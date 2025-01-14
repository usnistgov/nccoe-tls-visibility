#!/bin/sh
#
# Copyright (C) 2022-2024 Not for Radio, LLC
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
#
# SPDX-License-Identifier: 0BSD 
#

#
# Establish a user-specific chroot environment that permits only basic
# file operations via ssh or scp.  This works in concert with
# user-specific sshd configuration that minimizes capabilities and
# employs the sshd ChrootDirectory feature to limit the user to the
# chroot environment.
#
# The first two arguments to the script specify the chroot base
# directory and the user, respectively.  The optional third argument
# provides a regex to use when selecting entries from the main
# environment /etc/passwd and /etc/group files to replicate into the
# chroot environment.  The /etc/passwd and /etc/group files
# established in the chroot environment are used to identify the user
# when logging in as well as to decode file and directory ownership if
# 'ls' is used.  root and <chroot_user> are always included.
#
# An example companion sshd configuration stanza is shown below, where
# <chroot_base> and <chroot_user> are the first two arguments to this
# script
#
# Match User <chroot_user>
#	PasswordAuthentication no
#	AllowAgentForwarding no
#	AllowTcpForwarding no
#	X11Forwarding no
#	PermitTTY no
#	PermitUserRC no
#	ChrootDirectory <chroot_base>/<chroot_user>
#
# It is assumed that <chroot_user> has a home directory of
# /home/<chroot_user>, such that sshd will locate the authorized keys
# for the account in /home/<chroot_user>/.ssh/authorized_keys.
# Following authorization using one of the keys contained in that
# file, sshd will chroot to <chroot_base>/<chroot_user> and set the
# working directory to <chroot_base>/<chroot_user>/home/<chroot_user>,
# which will be referred to as <chroot_home>
#
# The user will be able to perform scp to locations under
# <chroot_home>, as well as execute the following commands via ssh:
#
#   cp ls mkdir mv rm rmdir
#
# An interactive shell will not be available due to 'PermitTTY no' in
# the user-specific sshd configuration
#
# Note that this script is not entirely generic, and may only apply to
# Ubuntu 20.04 in its current form due to assumptions regarding
# library directory structure, identification of nss libraries,
# location of locale and terminfo information, etc.
#

announce() {
    echo ">>>" $@
}

die() {
    echo "!!!" $@
    exit 1
}

#
# Create the given directory if it does not exist, including any
# missing parents
#
ensure_dir() {
    local dir_name="$1"

    if [ ! -d "${dir_name}" ] && [ ! -L "${dir_name}" ]; then
	mkdir -p "${dir_name}" || die "Failed to create dir ${dir_name}"
    fi
}

#
# Same as ensure_dir(), but relative to the chroot base directory
#
ensure_chroot_dir() {
    local chroot_rel_dir="$1"

    ensure_dir "${chroot_dir}${chroot_rel_dir}"
}

#
# Copy the given file in the main environment to the same path under
# the chroot base directory
#
copy_file_to_chroot() {
    local f="$1"
    local d=$(dirname "${f}")

    announce "Copying file ${f}"
    ensure_chroot_dir "${d}"
    cp -p "${f}" "${chroot_dir}${f}" || die "Failed to copy ${f} to ${chroot_dir}${f}"
}

#
# Recursively copy the given directory in the main environment to the
# same path under the chroot base directory
#
copy_dir_to_chroot() {
    local d="$1"

    announce "Copying dir ${d}"
    ensure_chroot_dir "${d}"
    cp -rp "${d}/" "${chroot_dir}${d}" || die "Failed to copy ${d} to ${chroot_dir}${d}"
}


[ $(id -u) -eq 0 ] || die "This script needs to be executed as root"

if [ $# -ne 2 ] && [ $# -ne 3 ]; then
    echo "usage: $0 chroot_base user [passwd_group_regex]"
    exit 1
fi

chroot_base="$1"
if ! echo "${chroot_base}" | grep -q '^/'; then
    announce "Adding leading '/' to ${chroot_base}"
    chroot_base="/${chroot_base}"
fi

chroot_user="$2"
id "${chroot_user}" > /dev/null 2> /dev/null || die "User ${chroot_user} does not exist"

passwd_group_regex_extra="$3"

chroot_dir="${chroot_base}/${chroot_user}"

home_dir="/home/${chroot_user}"
[ -d "${home_dir}" ] || die "${home_dir} does not exist"

chroot_home_dir="${chroot_dir}${home_dir}"

announce "Making chroot environment for user ${chroot_user} under ${chroot_dir}"

#
# The loop below builds the list of executables, and the shared
# libraries that they depend on, that are to be copied into the chroot
# environment
#
chroot_progs="cp ls mkdir mv rm rmdir rbash scp"
for p in ${chroot_progs}; do
    prog_path=$(which "${p}")
    prog_deps=$(ldd "${prog_path}" | grep -o -E '/[^ ]+')
    chroot_prog_paths="${chroot_prog_paths}
$(dirname ${prog_path})"
    chroot_copy_paths="${chroot_copy_paths}
${prog_path}
${prog_deps}"
done

#
# The loop below adds additional required shared libraries and their
# dependencies to the copy list.  These libraries are not identified
# as dependencies of the executables processed in the loop above as
# they are opened by libc using dlopen() rather than being linked in
# at load time via the dynamic linker
#
chroot_usr_libs="libnss3.so libnss_files.so.2"
arch=$(uname -m)
for lib in ${chroot_usr_libs}; do
    lib_path="/usr/lib/${arch}-linux-gnu/${lib}"
    lib_deps=$(ldd "${lib_path}" | grep -o -E '/[^ ]+')
    chroot_copy_paths="${chroot_copy_paths}
${lib_path}
${lib_deps}"
done

#
# Filter out blank lines and duplicates
#
chroot_prog_paths=$(echo  "${chroot_prog_paths}" | grep . | sort -u)
chroot_copy_paths=$(echo  "${chroot_copy_paths}" | grep . | sort -u)

#
# Ensure the user's .ssh dir and authorized_keys file exist in the
# main environment
#
user_ssh_dir="${home_dir}/.ssh"
ensure_dir "${user_ssh_dir}"
if [ ! -f "${user_ssh_dir}/authorized_keys" ]; then
    touch "${user_ssh_dir}/authorized_keys" || die "Failed to create user ssh key file ${user_ssh_dir}/authorized_keys"
    chown ${chroot_user}:${chroot_user} "${user_ssh_dir}/authorized_keys"
fi
chmod 700 "${user_ssh_dir}"
chown ${chroot_user}:${chroot_user} "${user_ssh_dir}"

#
# Create the chroot base directory if it does not already exist
#
ensure_chroot_dir ""

#
# Ensure /lib exists as a linkg to /usr/lib inside the chroot environment
#
ensure_chroot_dir "/usr/lib"
ln -s usr/lib ${chroot_dir}/lib

#
# Create the user's home directory
#
ensure_chroot_dir "${home_dir}"
chown ${chroot_user}:${chroot_user} "${chroot_home_dir}"


announce "Copying chroot programs and dependencies for user ${chroot_user}"
for f in ${chroot_copy_paths}; do
    copy_file_to_chroot "${f}"
done

ensure_chroot_dir "/etc"

announce "Creating /etc/passwd and /etc/group"
if [ -n "${passwd_group_regex_extra}" ]; then
    passwd_group_regex_extra="|${passwd_group_regex_extra}"
fi

grep -E "^(root|${chroot_user}${passwd_group_regex_extra}):" /etc/passwd > "${chroot_dir}/etc/passwd"
grep -E "^(root|${chroot_user}${passwd_group_regex_extra}):" /etc/group > "${chroot_dir}/etc/group"

announce "Creating /etc/nsswitch.conf"
chroot_nsswitch="${chroot_dir}/etc/nsswitch.conf"
cat <<EOF > ${chroot_nsswitch}
passwd: files
group: files
EOF

copy_dir_to_chroot "/usr/share/terminfo"
copy_dir_to_chroot "/usr/share/locale"

announce "Creating /dev entries"
ensure_chroot_dir "/dev"
mknod ${chroot_dir}/dev/null c 1 3
mknod ${chroot_dir}/dev/zero c 1 5
chmod 0666 ${chroot_dir}/dev/null
chmod 0666 ${chroot_dir}/dev/zero

#
# Restrict PATH to the minimum required to access the configured
# executables
#
announce "Making chroot .profile for user ${chroot_user}"
chroot_profile="${chroot_home_dir}/.profile"
cat <<EOF > ${chroot_profile}
#
# .profile for restricted shell
#
PATH=$(echo -n ${chroot_prog_paths} | tr "\n" ":")
EOF
