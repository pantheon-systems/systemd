#global gitcommit 9fa2f41

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        44
Release:        23%{?gitcommit:.git%{gitcommit}}%{?dist}.pantheon1
License:        GPLv2+
Group:          System Environment/Base
Summary:        A System and Service Manager
BuildRequires:  udev >= 179-2
BuildRequires:  libudev-devel >= 179-2
BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-luks-devel
BuildRequires:  dbus-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  vala >= 0.11
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgee06-devel
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  libacl-devel
BuildRequires:  intltool >= 0.40.0
BuildRequires:  gperf
BuildRequires:  xz-devel
BuildRequires:  kmod-devel >= 5

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  git

Requires(post): authconfig
Requires(post): coreutils
Requires(post): gawk
Requires:       dbus >= 1.4.6-3.fc15
Requires:       udev >= 179-2
Requires:       libudev >= 179-2
Requires:       initscripts >= 9.28
Requires:       filesystem >= 3
Conflicts:      selinux-policy < 3.9.16-12.fc15
Conflicts:      kernel < 2.6.35.2-9.fc14
Requires:       nss-myhostname
%if %{defined gitcommit}
# Snapshot tarball can be created using: ./make-git-shapshot.sh [gitcommit]
Source0:        %{name}-git%{gitcommit}.tar.xz
%else
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
%endif
# Adds support for the %%{_unitdir} macro
Source1:        macros.systemd
Source2:        systemd-sysv-convert
# Stop-gap, just to ensure things work out-of-the-box for this driver.
Source3:        udlfb.conf
# Stop-gap, just to ensure things work fine with rsyslog without having to change the package right-away
Source4:        listen.conf

Patch0001:      0001-util-never-follow-symlinks-in-rm_rf_children.patch
Patch0002:      0002-man-fix-parameter-name-for-sd_uid_xxx.patch
Patch0003:      0003-bmfmt-allow-passing-more-than-one-config-file-name.patch
Patch0004:      0004-modules-load-drop-lib-from-search-path-if-we-don-t-h.patch
Patch0005:      0005-sysctl-accept-multiple-passed-configuration-files.patch
Patch0006:      0006-man-updates-to-sysctl.d-5.patch
Patch0007:      0007-journal-react-with-immediate-rotation-to-a-couple-of.patch
Patch0008:      0008-journal-PAGE_SIZE-is-not-known-on-ppc-and-other-arch.patch
Patch0009:      0009-systemd-mount-the-securityfs-filesystem-at-early-sta.patch
Patch0010:      0010-main-added-support-for-loading-IMA-custom-policies.patch
Patch0011:      0011-man-systemd-cat-1-typo-fix.patch
Patch0012:      0012-binfmt-fix-apply-loop.patch
Patch0013:      0013-add-sparse-support-to-detect-endianness-bug.patch
Patch0014:      0014-update-TODO.patch
Patch0015:      0015-logind-extend-comment-about-X11-socket-symlink.patch
Patch0016:      0016-logind-close-FIFO-before-ending-sessions-cleanly.patch
Patch0017:      0017-man-minor-typo-in-reference-to-manual-page.patch
Patch0018:      0018-build-sys-fix-make-dist-check.patch
Patch0019:      0019-journalctl-loginctl-drop-systemd-prefix-in-binary-na.patch
Patch0020:      0020-build-sys-do-not-set-CFLAGS-directly.patch
Patch0021:      0021-build-sys-separate-ldflags-from-cflags.patch
Patch0022:      0022-man-don-t-claim-f-was-short-for-follow.patch
Patch0023:      0023-journalctl-add-local-switch.patch
Patch0024:      0024-cat-fix-priority-type.patch
Patch0025:      0025-units-get-rid-of-var-run.mount-and-var-lock.mount.patch
Patch0026:      0026-journal-properly-handle-if-we-interleave-files-with-.patch
Patch0027:      0027-job-fix-loss-of-ordering-with-restart-jobs.patch
Patch0028:      0028-job-add-debug-prints-where-job-type-gets-changed.patch
Patch0029:      0029-rename-etc-systemd-systemd-login-journal-d.conf-to-l.patch
Patch0030:      0030-bash-completion-update-naming-of-loginctl.patch
Patch0031:      0031-journal-decrease-default-mmap-window-size-to-allow-a.patch
Patch0032:      0032-journal-implicitly-add-code-location-to-all-messages.patch
Patch0033:      0033-install-check-for-proper-return-from-dirent_ensure_t.patch
Patch0034:      0034-Revert-socket-if-we-fail-to-create-an-instantiated-s.patch
Patch0035:      0035-analyze-Cosmetic-exit-when-the-bootup-is-not-yet-com.patch
Patch0036:      0036-systemctl-make-f-short-for-both-follow-and-force.patch
Patch0037:      0037-journal-in-json-and-export-mode-use-double-underscor.patch
Patch0038:      0038-fix-a-couple-of-AF_UNIX-connect-calls.patch
Patch0039:      0039-logind-log-with-AUTH-facility.patch
Patch0040:      0040-man-document-special-journal-fields.patch
Patch0041:      0041-man-update-documentation-of-special-units.patch
Patch0042:      0042-man-clarify-the-formatting-of-timestamps.patch
Patch0043:      0043-man-document-the-_TRANSPORT-journal-field.patch
Patch0044:      0044-journal-don-t-export-the-boot-id-twice-per-entry.patch
Patch0045:      0045-units-use-SYSTEMCTL-instead-of-hardcoded-paths.patch
Patch0046:      0046-build-sys-remove-vala-hack-which-did-not-allow-to-li.patch
Patch0047:      0047-units-direct-users-to-the-journal-for-logs-when-ente.patch
Patch0048:      0048-build-sys-add-a-few-missing-headers.patch
Patch0049:      0049-job-use-a-lookup-table-for-merging-of-job-types.patch
Patch0050:      0050-systemd-add-hardware-watchdog-support.patch
Patch0051:      0051-util-move-all-to-shared-and-split-external-dependenc.patch
Patch0052:      0052-util-move-ACL-code-into-internal-library.patch
Patch0053:      0053-build-sys-add-AM_CFLAGS-where-needed.patch
Patch0054:      0054-udev-fix-gcc-warnings-showing-up-after-adding-AM_CFL.patch
Patch0055:      0055-move-cgroup-util.-ch-to-shared.patch
Patch0056:      0056-move-libsystemd-capability.la-dep-from-basic-to-core.patch
Patch0057:      0057-use-libsystemd-id128.la-instead-of-source-file.patch
Patch0058:      0058-use-libsystemd-daemon.la-instead-of-source-file.patch
Patch0059:      0059-move-pager.-ch-to-shared.patch
Patch0060:      0060-move-list.h-macro.h-ioprio.h-to-shared.patch
Patch0061:      0061-watchdog-really-return-the-actual-watchdog-timeout.patch
Patch0062:      0062-dbus-add-data-argument-to-BusPropertySetCallback.patch
Patch0063:      0063-dbus-add-generic-DEFINE_BUS_PROPERTY_SET_ENUM-macro-.patch
Patch0064:      0064-dbus-make-the-service-property-StartLimitAction-writ.patch
Patch0065:      0065-fixup-for-missing-udev-convert-uaccess-to-a-builtin.patch
Patch0066:      0066-units-introduce-nss-user-lookup.target.patch
Patch0067:      0067-logs-show-fix-output-of-log-lines-lacking-comm.patch
Patch0068:      0068-systemctl-don-t-forward-poweroff-reboot-requests-to-.patch
Patch0069:      0069-shutdownd-rework-interface-allow-subscribing-to-sche.patch
Patch0070:      0070-pam_systemd-add-missing-libsystemd_audit.l.patch
Patch0071:      0071-build-sys-add-AM_LDFLAGS-where-needed.patch
Patch0072:      0072-build-sys-move-remaining-headers-out-EXTRA_DIST-inst.patch
Patch0073:      0073-split-selinux-label-operations-out-of-cgroup-util-so.patch
Patch0074:      0074-main-add-URL-to-cgroups-check-message.patch
Patch0075:      0075-machine-id-don-t-delete-runtime-machine-id-and-place.patch
Patch0076:      0076-main-drop-container-initrd-env-vars-from-inherited-s.patch
Patch0077:      0077-main-unset-some-bash-specific-environment-variables-.patch
Patch0078:      0078-move-libsystemd_core.la-sources-into-core.patch
Patch0079:      0079-put-acl.la-in-if-HAVE_ACL-and-rename-acl.-ch-to-acl-.patch
Patch0080:      0080-main-disarm-watchdog-when-preparing-for-reexecution.patch
Patch0081:      0081-polkit-temporarily-spawn-of-a-polkit-agent-in-termin.patch
Patch0082:      0082-tmpfiles-open-directories-with-O_NOATIME-to-preserve.patch
Patch0083:      0083-enable-proper-access-timestamps-on-all-tmpfs-mounts.patch
Patch0084:      0084-units-exclude-gettys-from-isolate-requests.patch
Patch0085:      0085-polkit-when-spawning-off-agent-wait-until-the-agent-.patch
Patch0086:      0086-One-can-specify-in-which-cgroup-hierarchies-a-system.patch
Patch0087:      0087-move-more-common-files-to-shared-and-add-them-to-sha.patch
Patch0088:      0088-unit-introduce-ConditionPathIsReadWrite.patch
Patch0089:      0089-units-run-sysctl-stuff-only-when-proc-sys-is-actuall.patch
Patch0090:      0090-units-start-vconsole-setup-only-if-there-s-actually-.patch
Patch0091:      0091-main-pass-original-environment-block-to-shutdown-bin.patch
Patch0092:      0092-execute-when-we-can-t-get-the-requested-rlimit-get-t.patch
Patch0093:      0093-journald-add-missing-flag-to-open.patch
Patch0094:      0094-nspawn-bind-mount-dev-nul-to-proc-kmsg-so-that-the-c.patch
Patch0095:      0095-rename-machine-id-main.c-tomacht-the-binary-and-move.patch
Patch0096:      0096-move-a-couple-of-test-.c-to-test.patch
Patch0097:      0097-build-sys-add-stub-makefiles-to-make-emacs-easier-to.patch
Patch0098:      0098-build-sys-move-a-few-things-into-more-appropriate-pl.patch
Patch0099:      0099-umount-don-t-try-to-umount-dev-console-since-we-are-.patch
Patch0100:      0100-build-sys-dbus-loop.h-is-not-used-by-the-core.patch
Patch0101:      0101-test-test-tools-should-still-be-in-the-src-directory.patch
Patch0102:      0102-umount-fix-build.patch
Patch0103:      0103-shutdown-move-shutdown-to-core-since-it-replaces-PID.patch
Patch0104:      0104-hostname-setup-move-to-core.patch
Patch0105:      0105-move-more-main-systemd-parts-to-core.patch
Patch0106:      0106-main-we-want-all-setup-functions-to-be-in-files-call.patch
Patch0107:      0107-rename-bridge.c-to-stdio-bridge.c-and-move-to-subdir.patch
Patch0108:      0108-detect-virt-beef-up-tool-considerably.patch
Patch0109:      0109-detect-virt-make-detect-virt-an-official-command.patch
Patch0110:      0110-machine-id-setup-add-the-usual-command-line-paramete.patch
Patch0111:      0111-detect-virt-print-none-if-no-virtualization-is-detec.patch
Patch0112:      0112-move-remainig-shared-stuff-to-shared.patch
Patch0113:      0113-move-libsystemd-id128-libsystemd-daemon-to-subdir.patch
Patch0114:      0114-build-sys-introduce-seperate-convenience-library-for.patch
Patch0115:      0115-getty-VC-devices-are-always-available-we-don-t-need-.patch
Patch0116:      0116-getty-skip-VC-gettys-if-the-VC-subsystem-is-not-avai.patch
Patch0117:      0117-build-sys-split-off-logs-show-into-its-own-convenien.patch
Patch0118:      0118-journal-fix-missing-variable-initialization.patch
Patch0119:      0119-machine-id-setup-avoid-cyclic-dependency-built-twice.patch
Patch0120:      0120-move-all-tools-to-subdirs.patch
Patch0121:      0121-build-sys-move-setup-out-of-shared-to-avoid-selinux-.patch
Patch0122:      0122-build-sys-create-top-level-directory-for-bash-comple.patch
Patch0123:      0123-build-sys-move-src-linux-to-src-shared-linux.patch
Patch0124:      0124-pam_systemd-add-dbus.la.patch
Patch0125:      0125-build-sys-remove-DBUS_LIBS-libsystemd-dbus.la-pulls-.patch
Patch0126:      0126-build-sys-use-check_PROGRAMS-for-test-.c.patch
Patch0127:      0127-udev-properly-hook-up-all-tests-to-make-check.patch
Patch0128:      0128-build-sys-move-systemd-analyze-into-its-own-subdir.patch
Patch0129:      0129-build-sys-execute-test-programs-with-make-check.patch
Patch0130:      0130-build-sys-drop-systemd-prefix-from-analyze-dir.patch
Patch0131:      0131-fix-a-couple-of-things-found-with-the-llvm-static-an.patch
Patch0132:      0132-udev-unpack-sysfs-test-tree-only-on-make-check-fix-t.patch
Patch0133:      0133-nspawn-fake-dev-kmsg-and-proc-kmsg-as-fifo.patch
Patch0134:      0134-manager-support-systems-lacking-dev-tty0.patch
Patch0135:      0135-loopback-handle-EPERM-more-gracefully.patch
Patch0136:      0136-audit-ignore-if-we-get-EPERM.patch
Patch0137:      0137-main-unset-some-more-env-vars.patch
Patch0138:      0138-units-do-binfmt-magic-only-when-proc-sys-is-writable.patch
Patch0139:      0139-logind-explicitly-check-for-dev-tty0.patch
Patch0140:      0140-unit-signal-explicitly-if-a-condition-failed-in-unit.patch
Patch0141:      0141-units-drop-audit-reference-from-description-of-utmp-.patch
Patch0142:      0142-dbus-expose-whether-we-have-a-hardware-watchdog-on-t.patch
Patch0143:      0143-dbus-automatically-send-out-changed-events-for-prope.patch
Patch0144:      0144-watchdog-make-watchdog-dbus-properties-writable.patch
Patch0145:      0145-nspawn-add-missing-include-lines.patch
Patch0146:      0146-polkit-spawn-agent-in-fallback-mode.patch
Patch0147:      0147-service-place-control-command-in-subcgroup-control.patch
Patch0148:      0148-build-sys-silence-the-xsltproc-output.patch
Patch0149:      0149-cgroup-if-a-controller-is-not-available-don-t-try-to.patch
Patch0150:      0150-manager-remove-unavailable-redundant-entries-from-de.patch
Patch0151:      0151-logind-add-shutdown-suspend-idle-inhibition-framewor.patch
Patch0152:      0152-logind-hook-up-inhibit-logic-with-idle-hint-logic.patch
Patch0153:      0153-cgls-don-t-show-empty-cgroups-by-default.patch
Patch0154:      0154-util-introduce-memdup.patch
Patch0155:      0155-systemctl-show-main-and-control-PID-explicitly-in-cg.patch
Patch0156:      0156-logind-remove-redundant-entries-from-logind-s-defaul.patch
Patch0157:      0157-man-Fix-a-few-typos.patch
Patch0158:      0158-configure.ac-Use-the-new-autoconf-field-to-set-the-p.patch
Patch0159:      0159-configure.ac-Use-a-auxiliar-directory-to-store-autog.patch
Patch0160:      0160-udev-replace-util_create_path-with-mkdir_parents.patch
Patch0161:      0161-mkdir-do-not-use-alloca-in-a-loop.patch
Patch0162:      0162-selinux-unify-systemd-and-udev-code.patch
Patch0163:      0163-silence-a-bunch-of-gcc-warnings.patch
Patch0164:      0164-udev-unify-dev-static-symlink-setup.patch
Patch0165:      0165-remove-MS_-which-can-not-be-combined-with-current-ke.patch
Patch0166:      0166-build-sys-move-dev-setup-to-label.la.patch
Patch0167:      0167-fix-typo-in-src-shared-install.c.patch
Patch0168:      0168-main-log-to-the-journal-in-container-mode-by-default.patch
Patch0169:      0169-mount-setup-don-t-log-with-LOG_ERROR-if-a-mount-that.patch
Patch0170:      0170-log-fix-LOG_TARGET_JOURNAL_OR_KMSG.patch
Patch0171:      0171-tmpfiles-fix-error-message.patch
Patch0172:      0172-manager-fix-comment.patch
Patch0173:      0173-job-allow-job_free-only-on-already-unlinked-jobs.patch
Patch0174:      0174-manager-simplify-transaction_abort.patch
Patch0175:      0175-job-job_uninstall.patch
Patch0176:      0176-manager-Transaction-as-an-object.patch
Patch0177:      0177-manager-split-transaction.-ch.patch
Patch0178:      0178-job-job_new-can-find-the-manager-from-the-unit.patch
Patch0179:      0179-job-jobs-shouldn-t-need-to-know-about-transaction-an.patch
Patch0180:      0180-transaction-do-not-add-installed-jobs-to-the-transac.patch
Patch0181:      0181-transaction-maintain-anchor_job.patch
Patch0182:      0182-transaction-change-the-linking-of-isolate-jobs-to-th.patch
Patch0183:      0183-transaction-simplify-transaction_find_jobs_that_matt.patch
Patch0184:      0184-transaction-avoid-garbage-collecting-the-anchor-job.patch
Patch0185:      0185-transaction-remove-the-anchor-link.patch
Patch0186:      0186-transaction-remove-a-couple-of-asserts.patch
Patch0187:      0187-job-separate-job_install.patch
Patch0188:      0188-transaction-rework-merging-with-installed-jobs.patch
Patch0189:      0189-transaction-remove-checks-for-installed.patch
Patch0190:      0190-dbus-job-allow-multiple-bus-clients.patch
Patch0191:      0191-transaction-add-starting-requirements-for-JOB_RESTAR.patch
Patch0192:      0192-watchdog-fix-default-configuration-fragment-for-watc.patch
Patch0193:      0193-nspawn-make-dev-kmsg-unavailable-in-the-container-bu.patch
Patch0194:      0194-mount-setup-ignore-common-container-bind-mounts.patch
Patch0195:      0195-nspawn-be-more-careful-when-initializing-the-hostnam.patch
Patch0196:      0196-log-include-syslog-identifier-in-default-log-propert.patch
Patch0197:      0197-util-fix-tty_is_vc_resolve-in-a-container-where-sys-.patch
Patch0198:      0198-loginctl-avoid-segfault-for-kill-session-and-kill-us.patch
Patch0199:      0199-container-spawn-a-getty-instead-of-a-sulogin-in-a-co.patch
Patch0200:      0200-login-assing-dev-console-logins-to-seat0.patch
Patch0201:      0201-default-to-v102-everywhere-instead-of-vt100-to-synch.patch
Patch0202:      0202-nspawn-add-b-switch-to-automatically-look-for-an-ini.patch
Patch0203:      0203-units-skip-root-fsck-if-the-root-directory-is-writab.patch
Patch0204:      0204-units-don-t-try-to-load-kernel-modules-if-CAP_SYS_MO.patch
Patch0205:      0205-nspawn-add-uuid-switch-to-allow-setting-the-machine-.patch
Patch0206:      0206-util-unify-getenv-logic-for-other-PID.patch
Patch0207:      0207-machine-id-fix-spelling.patch
Patch0208:      0208-transaction-add-missing-emacs-and-license-headers.patch
Patch0209:      0209-transaction-downgrade-warnings-about-masked-units.patch
Patch0210:      0210-mount-don-t-fail-if-fstab-doesn-t-exist.patch
Patch0211:      0211-units-remount-file-systems-only-if-etc-fstab-actuall.patch
Patch0212:      0212-job-the-status-messages-are-proper-sentences-hence-e.patch
Patch0213:      0213-hostname-if-there-s-already-a-hostname-set-when-PID-.patch
Patch0214:      0214-shutdown-don-t-try-to-shut-down-DM-devices-in-a-cont.patch
Patch0215:      0215-transaction-improve-readability.patch
Patch0216:      0216-transaction-fix-detection-of-cycles-involving-instal.patch
Patch0217:      0217-transaction-abort-does-not-need-to-use-recursive-del.patch
Patch0218:      0218-job-serialize-jobs-properly.patch
Patch0219:      0219-transaction-cancel-jobs-non-recursively-on-isolate.patch
Patch0220:      0220-readahead-rather-than-checking-for-virtualization-in.patch
Patch0221:      0221-man-rework-nspawn-man-page-to-suggest-yum-installroo.patch
Patch0222:      0222-service-introduce-Type-idle-and-use-it-for-gettys.patch
Patch0223:      0223-remount-consolidate-remount-api-vfs-and-remount-root.patch
Patch0224:      0224-shutdown-don-t-complain-if-we-cannot-lock-memory-to-.patch
Patch0225:      0225-nspawn-bind-mount-etc-resolv.conf-from-the-host-by-d.patch
Patch0226:      0226-nspawn-add-read-only-switch.patch
Patch0227:      0227-timedated-introduce-systemd-timedated-ntp.target-whi.patch
Patch0228:      0228-core-add-NOP-jobs-job-type-collapsing.patch
Patch0229:      0229-util-introduce-container_of-macro.patch
Patch0230:      0230-unit-add-new-dependency-type-RequiresMountsFor.patch
Patch0231:      0231-units-make-sure-var-is-writable-before-initializing-.patch
Patch0232:      0232-vconsole-fix-error-messages.patch
Patch0233:      0233-service-warn-if-a-dbus-name-is-specified-but-the-ser.patch
Patch0234:      0234-service-default-to-Type-dbus-if-BusName-is-specified.patch
Patch0235:      0235-units-explicit-Type-dbus-is-now-redundant.patch
Patch0236:      0236-vconsole-fix-some-error-messages.patch
Patch0237:      0237-hwclock-add-taint-flag-for-non-local-hwclock.patch
Patch0238:      0238-rc-local-generator-hook-halt-local-in-based-on-gener.patch
Patch0239:      0239-systemctl-get-rid-of-arg_immediate-and-fold-it-into-.patch
Patch0240:      0240-systemctl-print-a-nice-error-message-if-an-unprivile.patch
Patch0241:      0241-systemctl-allow-systemctl-reboot-ff-to-succeed-even-.patch
Patch0242:      0242-service-explicitly-remove-control-subcgroup-after-ea.patch
Patch0243:      0243-dbus-handle-invalid-enum-values-better.patch
Patch0244:      0244-cgroup-fix-alloca-misuse-in-cg_shorten_controllers.patch
Patch0245:      0245-readhead-temporarily-lower-the-kernel-s-read_ahead_k.patch
Patch0246:      0246-units-use-OOMScoreAdjust-in-the-unit-files-to-set-OO.patch
Patch0247:      0247-readahead-store-inode-numbers-in-pack-file.patch
Patch0248:      0248-man-clarify-_TRANSPORT.patch
Patch0249:      0249-systemd-analyze-add-a-user-option-to-support-user-in.patch
Patch0250:      0250-systemctl-fix-typo.patch
Patch0251:      0251-logind-implement-delay-inhibitor-locks-in-addition-t.patch
Patch0252:      0252-conf_files_list-files-add-do-not-canonicalize-file-n.patch
Patch0253:      0253-conf_files_list-split-out-conf_files_list_strv.patch
Patch0254:      0254-util-split-out-conf-file.-ch.patch
Patch0255:      0255-logind-fix-memory-leak.patch
Patch0256:      0256-util-split-out-hwclock.-ch.patch
Patch0257:      0257-util-split-out-path-util.-ch.patch
Patch0258:      0258-autogen.sh-undef-_FORTIFY_SOURCE-which-now-logs-warn.patch
Patch0259:      0259-logind-fix-test-inhibit.patch
Patch0260:      0260-logind-use-sleep-as-generic-term-for-suspend-hiberna.patch
Patch0261:      0261-sleep-implement-suspend-hibernate-as-first-class-tar.patch
Patch0262:      0262-logind-implement-suspend-hibernate-calls-with-inhibi.patch
Patch0263:      0263-main-simplify-unify-logic-for-parsing-runtime-boolea.patch
Patch0264:      0264-path-util-there-is-no-function-path_parent.patch
Patch0265:      0265-manager-introduce-SwitchRoot-bus-call-for-initrd-mai.patch
Patch0266:      0266-util-a-few-updates-for-rm_rf.patch
Patch0267:      0267-bash-completion-avoid-losing-backslashes-in-unit-nam.patch
Patch0268:      0268-bash-completion-use-printf-instead-of-echo.patch
Patch0269:      0269-main-fix-assertion-failure-due-to-use-of-ELEMENTSOF-.patch
Patch0270:      0270-main-fix-uninitialized-variable.patch
Patch0271:      0271-dbus-manager-fix-tainted-string.patch
Patch0272:      0272-units-do-not-quit-plymouth-too-early.patch
Patch0273:      0273-job-only-jobs-on-the-runqueue-can-be-run.patch
Patch0274:      0274-job-change-red-ABORT-status-to-yellow-DEPEND.patch
Patch0275:      0275-unit-print-the-color-status-marks-on-the-left.patch
Patch0276:      0276-unit-unit-type-dependent-status-messages.patch
Patch0277:      0277-job-report-the-status-of-first-half-of-JOB_RESTART-t.patch
Patch0278:      0278-job-info-message-if-JOB_VERIFY_ACTIVE-detects-an-ina.patch
Patch0279:      0279-core-add-extra-safety-check-before-switching-root.patch
Patch0280:      0280-systemctl-add-switch-root-verb.patch
Patch0281:      0281-namespace-make-PrivateTmp-apply-to-both-tmp-and-var-.patch
Patch0282:      0282-sd-login-update-header-docs-a-bit.patch
Patch0283:      0283-missing-Fix-broken-syscall-__NR_fanotify_mark.-on-pp.patch
Patch0284:      0284-install-fix-inverted-meaning-of-force-in-systemctl-e.patch
Patch0285:      0285-man-overwrite-vs.-override.patch
Patch0286:      0286-tmpfiles-if-we-are-supposed-to-write-a-string-to-a-f.patch
Patch0287:      0287-build-sys-fix-distcheck.patch
Patch0288:      0288-delta-add-systemd-delta-tool-to-find-overriden-confi.patch
Patch0289:      0289-switch-root-check-for-absolute-paths.patch
Patch0290:      0290-delta-add-missing-files.patch
Patch0291:      0291-delta-add-preset-dirs.patch
Patch0292:      0292-delta-Support-filtering-what-type-of-deltas-to-show.patch
Patch0293:      0293-delta-enums-are-much-cooler-than-defines.patch
Patch0294:      0294-F17-units-do-not-use-Type-idle-yet.patch
Patch0295:      0295-delta-use-same-nomenclature-for-equivalent-and-redir.patch
Patch0296:      0296-delta-introduce-arg_flags-field-to-follow-our-usual-.patch
Patch0297:      0297-delta-don-t-highlight-unchanged-files.patch
Patch0298:      0298-delta-drop-PHP-ism.patch
Patch0299:      0299-dbus-unit-always-load-the-unit-before-handling-a-mes.patch
Patch0300:      0300-systemctl-drop-useless-DBus-calls-from-systemctl-sho.patch
Patch0301:      0301-F17-Revert-logind-close-FIFO-before-ending-sessions-.patch
Patch0302:      0302-units-introduce-new-Documentation-field-and-make-use.patch
Patch0303:      0303-login-minor-typo-fix.patch
Patch0304:      0304-unit-introduce-RequiredBy-setting-in-Install-to-comp.patch
Patch0305:      0305-hostname-setup-also-consider-one-an-unset-hostname.patch
Patch0306:      0306-cryptsetup-a-few-simplifications.patch
Patch0307:      0307-service-make-the-fsck-pass-no-configurable.patch
Patch0308:      0308-main-try-a-bit-harder-to-find-an-init-process-to-exe.patch
Patch0309:      0309-cryptsetup-support-discards-TRIM.patch
Patch0310:      0310-journalctl-fix-built-in-usage-output.patch
Patch0311:      0311-sd-pam-Drop-uid-so-parent-signal-arrives-at-child.patch
Patch0312:      0312-util-fix-typo-in-newdup.patch
Patch0313:      0313-delta-fix-spelling-of-overridden.patch
Patch0314:      0314-main-corrected-do_switch_root.patch
Patch0315:      0315-util.c-add-in_initrd.patch
Patch0316:      0316-manager-only-serialize-the-timestamps-for-the-initra.patch
Patch0317:      0317-core-main.c-add-switchedroot-parameter.patch
Patch0318:      0318-core-main.c-do_switch_root-do-not-remove-the-old-roo.patch
Patch0319:      0319-core-main.c-handle-the-initrd-timestamp-differently-.patch
Patch0320:      0320-delta-delta.c-initialize-bottom-for-fail-state.patch
Patch0321:      0321-util-rm_rf_children-add-root_dev-parameter.patch
Patch0322:      0322-main-do_switch_root-do-not-recursively-remove-across.patch
Patch0323:      0323-switch-root-move-switch_root-call-into-its-own-.c-fi.patch
Patch0324:      0324-main-rename-a-few-fix-to-follow-general-naming-style.patch
Patch0325:      0325-util-rework-in_initrd-logic.patch
Patch0326:      0326-journald-fix-length-of-SYSLOG_IDENTIFIER.patch
Patch0327:      0327-journald-one-more-SYSLOG_IDENTIFIER-length-fix.patch
Patch0328:      0328-main-allow-system-wide-limits-for-services.patch
Patch0329:      0329-F17-fix-manpage-names.patch
Patch0330:      0330-man-relax-wording-in-journal-fields-7-a-bit.patch
Patch0331:      0331-systemd-analyze-switch-to-python-getopt-for-argument.patch
Patch0332:      0332-Fixed-handling-of-posix_fallocate-returned-value.patch
Patch0333:      0333-cgtop-change-default-depth-to-3.patch
Patch0334:      0334-service-schedule-JOB_RESTART-from-SERVICE_AUTO_RESTA.patch
Patch0335:      0335-service-actually-delay-auto-restart-if-another-job-i.patch
Patch0336:      0336-service-fix-auto-restart-handling-in-service_stop.patch
Patch0337:      0337-service-fix-auto-restart-handling-in-service_start.patch
Patch0338:      0338-mount-use-the-same-fstab-extension-option-syntax-eve.patch
Patch0339:      0339-main-properly-queue-default.target-after-switched-ro.patch
Patch0340:      0340-journal-crash-when-filesystem-is-low-on-space.patch
Patch0341:      0341-util-make-sure-to-fstatat-at-most-once-in-rm_rf_chil.patch
Patch0342:      0342-switch-root-do-not-use-close-old_root_fd-after-rm_rf.patch
Patch0343:      0343-logind-fix-write-out-of-user-state-file.patch
Patch0344:      0344-main-only-fall-back-to-bin-sh-in-case-sbin-init-does.patch
Patch0345:      0345-execute-use-a-much-lower-idle-timeout-that-default-t.patch
Patch0346:      0346-journal-log-journal-internal-messages-to-kmsg.patch
Patch0347:      0347-log-make-sure-generators-never-log-into-the-journal-.patch
Patch0348:      0348-readahead-avoid-activating-the-journal-by-accident-l.patch
Patch0349:      0349-readahead-avoid-running-of-readahead-services-if-rea.patch
Patch0350:      0350-man-properly-document-FsckPassNo-for-mount-units.patch
Patch0351:      0351-journal-don-t-complain-if-SELinux-userspace-is-avail.patch
Patch0352:      0352-units-fix-file-syntax.patch
Patch0353:      0353-service-for-Type-idle-units-consider-START_PRE-START.patch
Patch0354:      0354-main-add-configuration-option-to-alter-capability-bo.patch
Patch0355:      0355-man-systemctl.xml-Add-missing-space-for-stopcommand.patch
Patch0356:      0356-bash-Reflect-new-name-of-loginctl-in-bash-completion.patch
Patch0357:      0357-cgtop-work-even-if-not-all-cgroups-are-available.patch
Patch0358:      0358-capabilities-when-dropping-capabilities-system-wide-.patch
Patch0359:      0359-sleep-print-nice-messages-right-before-and-right-aft.patch
Patch0360:      0360-journald-ignore-messages-read-from-proc-kmsg-that-we.patch
Patch0361:      0361-build-sys-fix-built-with-disable-logind.patch
Patch0362:      0362-journalctl-for-now-complain-if-more-than-one-match-i.patch
Patch0363:      0363-journalctl-support-usr-bin-nginx-etc.patch
Patch0364:      0364-journalctl-check-first-if-match-is-a-path-name.patch
Patch0365:      0365-journal-don-t-allow-adding-invalid-matches-to-the-co.patch
Patch0366:      0366-shutdown-Don-t-skip-bind-mounts-on-shutdown.patch
Patch0367:      0367-selinux-downgrade-database-load-time-message-to-LOG_.patch
Patch0368:      0368-login-properly-detect-MIMO-USB-displays.patch
Patch0369:      0369-journald-properly-handle-if-we-have-no-PID-in-a-kmsg.patch
Patch0370:      0370-systemctl-introduce-systemctl-man-to-show-man-page-f.patch
Patch0371:      0371-util-introduce-a-proper-nsec_t-and-make-use-of-it-wh.patch
Patch0372:      0372-main-allow-setting-of-timer-slack-for-PID-1.patch
Patch0373:      0373-util-don-t-require-libcap-when-building-libsystemd-s.patch
Patch0374:      0374-mkdir-append-_label-to-all-mkdir-calls-that-explicit.patch
Patch0375:      0375-mkdir-provide-all-functions-with-and-without-selinux.patch
Patch0376:      0376-units-add-Documentation-field-to-console-getty.servi.patch
Patch0377:      0377-man-add-documentation-for-the-binfmt-modules-load-sy.patch
Patch0378:      0378-main-Silence-gcc-warning.patch
Patch0379:      0379-logind-properly-clean-up-user-cgroups-when-they-run-.patch
Patch0380:      0380-logind-add-new-user-state-closing.patch
Patch0381:      0381-build-sys-split-off-D-Bus-requires-from-selinux-conv.patch
Patch0382:      0382-sleep-Don-t-call-execute_directory-on-a-binary.patch
Patch0383:      0383-logind-interpret-the-can_sleep-return-value-properly.patch
Patch0384:      0384-logind-fix-indentation.patch
Patch0385:      0385-man-write-man-page-for-systemd-logind.patch
Patch0386:      0386-man-document-systemd-journal.patch
Patch0387:      0387-journal-support-changing-the-console-tty-to-forward-.patch
Patch0388:      0388-journal-allow-setting-of-a-cutoff-log-level-for-disk.patch
Patch0389:      0389-units-fix-man-section.patch
Patch0390:      0390-fix-typo.patch
Patch0391:      0391-missing-define-MS_STRICTATIME-if-not-defined-already.patch
Patch0392:      0392-systemd-detect-virt-fix-option-quiet-requires-an-arg.patch
Patch0393:      0393-logind-punt-duplicate-definition-of-InhibitWhat.patch
Patch0394:      0394-unit-name-never-create-a-unit-name-with-a-leading.patch
Patch0395:      0395-remove-support-for-deprecated-proc-self-oom_adj.patch
Patch0396:      0396-systemctl-rename-man-to-help.patch
Patch0397:      0397-silence-gcc-warning-on-32-bit.patch
Patch0398:      0398-readahead-Add-tool-to-analyze-the-contents-of-the-pa.patch
Patch0399:      0399-Revert-F17-units-do-not-use-Type-idle-yet.patch
Patch0400:      0400-units-avoid-redundant-VT-clearing-by-agetty.patch
Patch0401:      0401-units-add-systemd-debug-shell.service.patch
Patch0402:      0402-systemd-debug-shell-add-to-POTFILES.skip.patch
Patch0403:      0403-man-systemd-tmpfiles-document-proper-config-file-sta.patch
Patch0404:      0404-man-replace-tabs-with-spaces.patch
Patch0405:      0405-tmpfiles-allow-to-specify-basename-only-systemd-tmpf.patch
Patch0406:      0406-tmpfiles-print-error-if-basename-lookup-fails-docume.patch
Patch0407:      0407-tmpfiles-fix-error-message.patch
Patch0408:      0408-logind-fix-check-for-multiple-sessions.patch
Patch0409:      0409-journal-file-fix-mmap-leak.patch
Patch0410:      0410-man-fix-sysytemd-typos.patch
Patch0411:      0411-F17-fix-manpage-name-typo.patch
Patch0412:      0412-systemctl-will-print-warning-when-stopping-unit.patch
Patch0413:      0413-systemctl-style-fixes-for-the-previous-patch.patch
Patch0414:      0414-systemctl-remove-is_socket_listening.patch
Patch0415:      0415-systemctl-fix-iteration-in-check_listening_sockets.patch
Patch0416:      0416-systemctl-warn-about-all-active-triggers-not-just-so.patch
Patch0417:      0417-unit-name-introduce-unit_dbus_path_from_name.patch
Patch0418:      0418-tmpfiles-create-char-devices-with-correct-SELinux-co.patch
Patch0419:      0419-systemctl-clearer-error-message-for-missing-install-.patch
Patch0420:      0420-service-timeout-for-oneshot-services.patch
Patch0421:      0421-logind-more-robust-handling-of-VT-less-systems.patch
Patch0422:      0422-journal-replace-arena-offset-by-header-size.patch
Patch0423:      0423-journal-add-basic-object-definition-for-signatures.patch
Patch0424:      0424-journal-correct-list-link-up-on-hash-collisions.patch
Patch0425:      0425-F17-fix-libsystemd-journal-symver-script.patch
Patch0426:      0426-journal-expose-and-make-use-of-cutoff-times-of-journ.patch
Patch0427:      0427-journal-fix-SD_JOURNAL_SYSTEM_ONLY-flag.patch
Patch0428:      0428-journal-rotate-on-SIGUSR2.patch
Patch0429:      0429-journal-fix-monotonic-seeking.patch
Patch0430:      0430-systemd-return-error-when-asked-to-stop-unknown-unit.patch
Patch0431:      0431-F17-Temporarily-revert-systemd-return-error-when-ask.patch
Patch0432:      0432-logind-expose-CanGraphical-and-CanTTY-properties-on-.patch
Patch0433:      0433-logind-introduce-a-state-for-session-being-one-of-on.patch
Patch0434:      0434-man-document-new-sd_session_get_state-call.patch
Patch0435:      0435-login-wrap-CanTTY-and-CanGraphical-seat-attributes-i.patch
Patch0436:      0436-preset-don-t-look-for-preset-files-in-lib-unless-usr.patch
Patch0437:      0437-service-fix-incorrect-argument.patch
Patch0438:      0438-service-pass-via-FAILED-DEAD-before-going-to-AUTO_RE.patch
Patch0439:      0439-core-make-systemd.confirm_spawn-1-actually-work.patch
Patch0440:      0440-modules-load-parse-driver-rd.driver-kernel-command-l.patch
Patch0441:      0441-modules-load-don-t-fail-on-builtin-modules-better-pr.patch
Patch0442:      0442-modules-load-fix-return-value.patch
Patch0443:      0443-modules-load-use-correct-va_list-logging-function.patch
Patch0444:      0444-mount-split-adding-of-extras-from-mount_load.patch
Patch0445:      0445-mount-load-only-if-we-there-s-mountinfo-or-fragment.patch
Patch0446:      0446-remount-fs-also-remount-usr-according-to-fstab.patch
Patch0447:      0447-manager-serialize-deserialize-job-counters-across-re.patch
Patch0448:      0448-timedated-replace-systemd-timedated-ntp.target-logic.patch
Patch0449:      0449-timedate-fix-ntp-units-comment.patch
Patch0450:      0450-units-rename-systemd-debug-shell.service-to-debug-sh.patch
Patch0451:      0451-modules-load-rename-kernel-command-line-option-to-rd.patch
Patch0452:      0452-timedated-replace-ntp-units-file-with-an-ntp-units.d.patch
Patch0453:      0453-journal-fix-iteration-through-journal-if-one-file-is.patch
Patch0454:      0454-journald-handle-proc-kmsg-reads-returning-0-more-nic.patch
Patch0455:      0455-timedate-uniq-ify-ntp-units-list.patch
Patch0456:      0456-load-fragment-a-few-modernizations.patch
Patch0457:      0457-hashmap-make-hashmap_clear-work-on-NULL-hashmaps.patch
Patch0458:      0458-mount-setup-don-t-complain-if-we-try-to-fix-the-labe.patch
Patch0459:      0459-man-explain-StartLimitRate-in-conjunction-with-Resta.patch
Patch0460:      0460-man-clarify-that-StartLimitInterval-also-applies-to-.patch
Patch0461:      0461-service-flush-the-start-counter-in-systemctl-reset-f.patch
Patch0462:      0462-man-document-Restart-a-bit-more.patch
Patch0463:      0463-man-update-man-pages-to-reflect-the-driver-to-load-m.patch
Patch0464:      0464-paranoia-refuse-rm_rf.patch
Patch0465:      0465-unit-Move-UnitType-definitions-from-core-unit.c-to-s.patch
Patch0466:      0466-systemctl-check-the-argument-to-t-for-invalid-values.patch
Patch0467:      0467-unit-name-remove-unit_name_is_valid_no_type-and-move.patch
Patch0468:      0468-unit-get-rid-of-UnitVTable.suffix-which-is-now-unuse.patch
Patch0469:      0469-unit-Move-UnitLoadState-definitions-from-core-unit.c.patch
Patch0470:      0470-systemctl-filter-shown-units-by-their-load-state.patch
Patch0471:      0471-mount-fix-for-complex-automounts.patch
Patch0472:      0472-util-add-extra-safety-check-to-in_initrd.patch
Patch0473:      0473-journal-fix-interleaving-of-files-with-different-tim.patch
Patch0474:      0474-journal-fix-bisection-logic-for-first-entry.patch
Patch0475:      0475-journal-fix-bad-memory-access.patch
Patch0476:      0476-journal-fix-seeking-by-realtime-seqnum.patch
Patch0477:      0477-journal-check-fields-we-search-for-more-carefully.patch
Patch0478:      0478-util-temporarily-ignore-SIGHUP-while-we-are-issuing-.patch
Patch0479:      0479-container-when-shutting-down-in-a-container-don-t-de.patch
Patch0480:      0480-unit-rename-BindTo-to-BindsTo.patch
Patch0481:      0481-journal-align-byte-buffer-that-gets-cased-to-an-obje.patch
Patch0482:      0482-aquire_terminal-fix-uninitialized-variable.patch
Patch0483:      0483-core-fix-name-of-dbus-call-parameter.patch
Patch0484:      0484-journald-don-t-enforce-monotonicity-of-realtime-cloc.patch
Patch0485:      0485-journal-use-tail-head-timestamps-from-header-for-cut.patch
Patch0486:      0486-journal-actually-set-archived-files-to-archived-stat.patch
Patch0487:      0487-service-make-start-jobs-wait-not-fail-when-an-automa.patch
Patch0488:      0488-service-don-t-print-a-warning-if-we-are-in-autoresta.patch
Patch0489:      0489-journald-don-t-choke-on-journal-files-with-no-cutoff.patch
Patch0490:      0490-journal-rotate-busy-files-away-when-we-try-to-write-.patch
Patch0491:      0491-journalctl-fix-assertion-failure-in-ellipsize_mem.patch
Patch0492:      0492-logind-fix-operation-precedence-mix-up.patch
Patch0493:      0493-systemctl-use-color-specification-understood-by-dot.patch
Patch0494:      0494-rules-avoid-mounting-raid-devices-too-early.patch
Patch0495:      0495-conf-files-continue-searching-if-one-dir-fails.patch
Patch0496:      0496-F17-restore-device-units-for-dev-ttyX.patch
Patch0497:      0497-systemd-return-error-when-asked-to-stop-unknown-unit.patch
Patch0498:      0498-modules-load-fix-kernel-cmdline-parsing.patch
Patch0499:      0499-units-add-the-modules-load-cmdline-parameters-to-the.patch
Patch0500:      0500-F17-fix-fstab-mounts.patch
Patch0501:      0501-Revert-timedate-uniq-ify-ntp-units-list.patch
Patch0502:      0502-Revert-timedated-replace-ntp-units-file-with-an-ntp-.patch
Patch0503:      0503-Revert-timedate-fix-ntp-units-comment.patch
Patch0504:      0504-Revert-timedated-replace-systemd-timedated-ntp.targe.patch
Patch0505:      0505-systemd-added-new-dependency-PartOf.patch
Patch0506:      0506-man-rewrite-the-description-of-PartOf.patch
Patch0507:      0507-dbus-unit-expose-PartOf-ConsistsOf-properties.patch
Patch0508:      0508-unit-make-the-table-of-inverse-deps-symmetric.patch
Patch0509:      0509-unit-add-missing-deps-in-unit_dependency_table.patch
Patch0510:      0510-systemd-enable-disable-instances-of-template.patch
Patch0511:      0511-logs-show-fix-OOM-path.patch
Patch0512:      0512-systemctl-automatically-turn-paths-and-unescaped-uni.patch
Patch0513:      0513-cryptsetup-fix-escaping-when-generating-cryptsetup-u.patch
Patch0514:      0514-systemctl-append-.service-to-unit-names-lacking-suff.patch
Patch0515:      0515-rules-99-systemd.rules.in-ENV-SYSTEMD_READY-0-for-in.patch
Patch0516:      0516-99-systemd.rules.in-ignore-nbd-in-the-add-uevent.patch
Patch0517:      0517-automount-print-mount-point-in-debug-message.patch
Patch0518:      0518-journald-fixed-memory-leak.patch
Patch0519:      0519-logs-show-fix-off-by-one-error.patch
Patch0520:      0520-shutdown-allow-to-specify-broadcast-message-when-can.patch
Patch0521:      0521-sysctl-apply-configuration-at-once.patch
Patch0522:      0522-systemd-introduced-new-timeout-types.patch
Patch0523:      0523-fix-a-couple-of-issues-found-with-llvm-analyze.patch
Patch0524:      0524-shared-utf8-mark-char-as-const.patch
Patch0525:      0525-shared-util-refactor-fstab_node_to_udev_node.patch
Patch0526:      0526-shared-util-add-fstab-support-for-partuuid-partlabel.patch
Patch0527:      0527-login-check-return-of-parse_pid-and-parse_uid.patch
Patch0528:      0528-unit-don-t-allow-units-to-be-gc-ed-that-still-are-re.patch
Patch0529:      0529-unit-add-new-ConditionHost-condition-type.patch
Patch0530:      0530-condition-add-ConditionFileNotEmpty.patch
Patch0531:      0531-unit-name-rework-unit_name_replace_instance-function.patch
Patch0532:      0532-pam-Add-session-class-to-the-debug-log.patch
Patch0533:      0533-tmpfiles-support-globbing-for-w-option.patch
Patch0534:      0534-systemctl-direct-the-user-to-list-unit-files-from-th.patch
Patch0535:      0535-tmpfiles-plug-file-descriptor-leak.patch
Patch0536:      0536-update-utmp-Don-t-error-out-on-runlevel-updates-if-u.patch
Patch0537:      0537-install-append-.service-when-enable-disable.-is-call.patch
Patch0538:      0538-systemctl-minor-coding-style-fixes.patch
Patch0539:      0539-socket-prevent-signed-integer-overflow.patch
Patch0540:      0540-tmpfiles-use-write-2-for-the-w-action.patch
Patch0541:      0541-service-don-t-hit-an-assert-if-a-service-unit-change.patch
Patch0542:      0542-hwclock-always-set-the-kernel-s-timezone.patch
Patch0543:      0543-conf-parser-don-t-unescape-parsed-configuration-stri.patch
Patch0544:      0544-log-avoid-function-loop.patch
Patch0545:      0545-target-imply-default-ordering-for-PartsOf-deps-as-we.patch
Patch0546:      0546-unit-fix-f-resolving.patch
Patch0547:      0547-mount-notify-the-user-if-we-over-mount-a-non-empty-d.patch
Patch0548:      0548-automount-also-whine-if-an-automount-directory-is-no.patch
Patch0549:      0549-mount-reword-directory-empty-warning-a-bit.patch
Patch0550:      0550-timedated-unregister-the-right-bus-service.patch
Patch0551:      0551-util-make-sure-heap-allocators-fail-when-array-alloc.patch
Patch0552:      0552-util-define-union-dirent_storage-and-make-use-of-it-.patch
Patch0553:      0553-util-overflow-hardening.patch
Patch0554:      0554-util-fix-overflow-checks.patch
Patch0555:      0555-shared-call-va_end-in-all-cases.patch
Patch0556:      0556-cgtop-missing.patch
Patch0557:      0557-logind-check-return-value-log-warning-on-error.patch
Patch0558:      0558-login-check-return-value-of-session_get_idle_hint.patch
Patch0559:      0559-locale-make-sure-that-l-is-freed.patch
Patch0560:      0560-modules-load-initalize-files-to-null.patch
Patch0561:      0561-sysctl-fix-error-code-handling.patch
Patch0562:      0562-login-missing-break-for-getopt-ARG_NO_ASK_PASSWORD-i.patch
Patch0563:      0563-hwclock-add-missing-OOM-check.patch
Patch0564:      0564-sysctl-always-return-the-last-error-we-encountered.patch
Patch0565:      0565-rules-only-mark-MD-disks-not-partitions-with-SYSTEMD.patch
Patch0566:      0566-tmpfiles-restore-previous-behavior-for-F-f.patch
Patch0567:      0567-shared-fail-mkdir_p-if-the-target-exists-and-is-not-.patch
Patch0568:      0568-sysctl-avoiding-exiting-with-error-on-EEXIST.patch
Patch0569:      0569-systemctl-don-t-mangle-name-when-it-is-a-path.patch
Patch0570:      0570-core-allow-Type-oneshot-services-to-have-ExecReload.patch
Patch0571:      0571-systemctl-append-.service-when-unit-does-not-have-va.patch
Patch0572:      0572-mount-don-t-try-to-initialize-extra-deps-for-mount-u.patch
Patch0573:      0573-udev-support-multiple-entries-for-ENV-SYSTEMD_ALIAS-.patch
Patch0574:      0574-Properly-handle-device-aliases-used-as-dependencies.patch
Patch0575:      0575-readahead-fix-fd-validity-check.patch
Patch0576:      0576-mount-make-sure-m-where-is-set-before-unit_add_exec_.patch
Patch0577:      0577-job-avoid-recursion-into-transaction-code-from-job-c.patch
Patch0578:      0578-sysctl-parse-all-keys-in-a-config-file.patch
Patch0579:      0579-add-libsystemd-id128-dependency-for-libsystemd-core..patch
Patch0580:      0580-mount-setup-change-system-mount-propagation-to-share.patch
Patch0581:      0581-shutdown-recursively-mark-root-as-private-before-piv.patch
Patch0582:      0582-switch-root-remount-to-MS_PRIVATE.patch
Patch0583:      0583-namespace-rework-namespace-support.patch
Patch0584:      0584-nspawn-namespaces-make-sure-we-recursively-bind-moun.patch
Patch0585:      0585-umount-MS_MGC_VAL-is-so-90s.patch
Patch1001:      1001-rlimit_nofile.patch

# For sysvinit tools
Obsoletes:      SysVinit < 2.86-24, sysvinit < 2.86-24
Provides:       SysVinit = 2.86-24, sysvinit = 2.86-24
Provides:       sysvinit-userspace
Provides:       systemd-sysvinit
Obsoletes:      systemd-sysvinit
Obsoletes:      upstart < 1.2-3
Obsoletes:      upstart-sysvinit < 1.2-3
Conflicts:      upstart-sysvinit
Obsoletes:      readahead < 1:1.5.7-3
Provides:       readahead = 1:1.5.7-3
Provides:       /bin/systemctl
Provides:       /sbin/shutdown
Obsoletes:      systemd-units < 38-5
Provides:       systemd-units = %{version}-%{release}
# for the systemd-analyze split:
Obsoletes:      systemd < 38-5
# old nfs-server.service forked daemons from ExecStartPre/Post:
Conflicts:      nfs-utils < 1:1.2.6
# usage of 'systemctl stop' on a non-existent unit in ExecStartPre:
Conflicts:      rsyslog < 5.8.10-2
Conflicts:      syslog-ng < 3.2.5-15

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package devel
Group:          System Environment/Base
Summary:        Development headers for systemd
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and auxiliary files for developing applications for systemd.

%package gtk
Group:          System Environment/Base
Summary:        Graphical frontend for systemd
Requires:       %{name} = %{version}-%{release}
Requires:       polkit

%description gtk
Graphical front-end for systemd.

%package sysv
Group:          System Environment/Base
Summary:        SysV tools for systemd
Requires:       %{name} = %{version}-%{release}

%description sysv
SysV compatibility tools for systemd

%package analyze
Group:          System Environment/Base
Summary:        Tool for processing systemd profiling information
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-python
Requires:       pycairo
# for the systemd-analyze split:
Obsoletes:      systemd < 38-5

%description analyze
'systemd-analyze blame' lists which systemd unit needed how much time to finish
initialization at boot.
'systemd-analyze plot' renders an SVG visualizing the parallel start of units
at boot.

%prep
%setup -q %{?gitcommit:-n %{name}-git%{gitcommit}}
git init
git config user.email "systemd-owner@fedoraproject.org"
git config user.name "systemd cabal"
git add .
git commit -m "base release %{version}"
git am %{patches}

%build
%{?gitcommit: ./autogen.sh }
autoreconf -i
%configure --with-distro=fedora --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/%{_sbindir}
ln -s ../lib/systemd/systemd %{buildroot}%{_sbindir}/init
ln -s ../lib/systemd/systemd %{buildroot}%{_bindir}/systemd
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/reboot
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/halt
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/poweroff
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/shutdown
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/telinit
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}/etc/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/syslog.target.wants

# Make sure the user generators dir exists too
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-generators

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/timezone
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Install RPM macros file for systemd
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/

# Install SysV conversion tool for systemd
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/

# Install modprobe fragment
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/modprobe.d/

# Install rsyslog fragment
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/rsyslog.d/

# To avoid making life hard for Rawhide-using developers, don't package the
# kernel.core_pattern setting until systemd-coredump is a part of an actual
# systemd release and it's made clear how to get the core dumps out of the
# journal.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/coredump.conf

# Let rsyslog read from /proc/kmsg for now
sed -i -e 's/\#ImportKernel=yes/ImportKernel=no/' %{buildroot}%{_sysconfdir}/systemd/systemd-journald.conf

# Add backward-compatible command names
ln -s loginctl %{buildroot}%{_bindir}/systemd-loginctl
ln -s journalctl %{buildroot}%{_bindir}/systemd-journalctl
ln -s systemctl %{buildroot}%{_bindir}/systemd-systemctl

# Short-term workaround for bz#834118 - s390(x) have no VTs
%ifarch s390 s390x
find %{buildroot}%{_prefix}/lib -name '*vconsole*' -delete
%endif

# debug-shell.service is the new name. Provide a compat symlink in F17.
ln -s debug-shell.service %{buildroot}%{_prefix}/lib/systemd/system/systemd-debug-shell.service

%post
/sbin/ldconfig
/usr/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
/usr/lib/systemd/systemd-random-seed save > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

# Make sure pam_systemd is enabled
if ! /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac >/dev/null 2>&1 || ! [ -h /etc/pam.d/system-auth ] ; then
        /usr/sbin/authconfig --update --nostart >/dev/null 2>&1 || :

        # Try harder
        /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac >/dev/null 2>&1 || /usr/sbin/authconfig --updateall --nostart >/dev/null 2>&1 || :
fi

# Stop-gap until rsyslog.rpm does this on its own. (This is supposed
# to fail when the link already exists)
/bin/ln -s /usr/lib/systemd/system/rsyslog.service /etc/systemd/system/syslog.service >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/usr/lib/systemd/system/graphical.target"
        else
                target="/usr/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" /etc/systemd/system/default.target >/dev/null 2>&1 || :

        # Enable the services we install by default.
        /bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :
else
        # This systemd service does not exist anymore, we now do it
        # internally in PID 1
        /bin/rm -f /etc/systemd/system/sysinit.target.wants/hwclock-load.service >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload > /dev/null 2>&1 || :
        /bin/systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target >/dev/null 2>&1 || :
fi

%triggerun -- systemd-units < 38-5
mv /etc/systemd/system/default.target /etc/systemd/system/default.target.save >/dev/null 2>&1 || :

%triggerpostun -- systemd-units < 38-5
mv /etc/systemd/system/default.target.save /etc/systemd/system/default.target >/dev/null 2>&1
/bin/systemctl enable \
        getty@.service \
        remote-fs.target \
        systemd-readahead-replay.service \
        systemd-readahead-collect.service

%files
%doc %{_docdir}/systemd
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/bash_completion.d
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/system-generators
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%dir %{_datadir}/systemd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/systemd-logind.conf
%config(noreplace) %{_sysconfdir}/systemd/systemd-journald.conf
%{_sysconfdir}/bash_completion.d/systemd-bash-completion.sh
%{_sysconfdir}/rpm/macros.systemd
%{_sysconfdir}/xdg/systemd
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%ghost %config(noreplace) %{_sysconfdir}/timezone
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
%config(noreplace) %{_sysconfdir}/rsyslog.d/listen.conf
%{_prefix}/lib/systemd/systemd
%{_bindir}/systemd
%{_bindir}/systemctl
%{_bindir}/loginctl
%{_bindir}/journalctl
%{_bindir}/systemd-notify
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-systemctl
%{_bindir}/systemd-loginctl
%{_bindir}/systemd-journalctl
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-readahead-analyze
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%{_prefix}/lib/systemd/systemd-*
%{_prefix}/lib/udev/rules.d/*.rules
%{_prefix}/lib/systemd/system-generators/systemd-cryptsetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-getty-generator
%{_prefix}/lib/systemd/system-generators/systemd-rc-local-generator
%{_libdir}/security/pam_systemd.so
%{_libdir}/libsystemd-daemon.so.*
%{_libdir}/libsystemd-login.so.*
%{_libdir}/libsystemd-journal.so.*
%{_libdir}/libsystemd-id128.so.*
%{_sbindir}/init
%{_sbindir}/reboot
%{_sbindir}/halt
%{_sbindir}/poweroff
%{_sbindir}/shutdown
%{_sbindir}/telinit
%{_sbindir}/runlevel
%{_mandir}/man1/*
%exclude %{_mandir}/man1/systemadm.*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/pkgconfig/systemd.pc
%config(noreplace) %{_sysconfdir}/modprobe.d/udlfb.conf

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files gtk
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*

%files devel
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_libdir}/libsystemd-journal.so
%{_libdir}/libsystemd-id128.so
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/sd-readahead.h
%{_includedir}/systemd/sd-shutdown.h
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc
%{_libdir}/pkgconfig/libsystemd-journal.pc
%{_libdir}/pkgconfig/libsystemd-id128.pc
%{_mandir}/man3/*

%files sysv
%{_bindir}/systemd-sysv-convert

%files analyze
%{_bindir}/systemd-analyze

%changelog
* Wed Dec 19 2012 Michal Schmidt <mschmidt@redhat.com> - 44-23
- Change mount propagation to shared by default. Should fix umounting of
  filesystems when PrivateTmp services are running.
- Resolves: #851970

* Tue Dec 04 2012 Karsten Hopp <karsten@redhat.com> - 44-22
- fix build on ppc, similar to 
  http://lists.freedesktop.org/archives/systemd-devel/2012-September/006424.html

* Fri Oct 26 2012 Michal Schmidt <mschmidt@redhat.com> - 44-21
- Fixes from upstream v195+:
- Don't forbid ExecReload in oneshot units.
- various fixes
- Resolves: #866346, #868603, #869779, fdo#52580

* Fri Oct 12 2012 Michal Schmidt <mschmidt@redhat.com> - 44-20
- Revert the ntp migration code. Not going to do it in F17.
- Backports from upstream v194+:
- PartOf= dependencies
- enabling/disabling of instantiated units
- usability improvements for systemctl:
  - systemctl status /home
  - systemctl status /dev/foobar
  - implied .service suffix
- new timeouts TimeoutStartSec=, TimeoutStopSec=
- understand PARTUUID=, PARTLABEL= in fstab
- new conditions ConditionHost=, ConditionFileNotEmpty=
- tmpfiles: globbing support with 'w' mode
- various fixes
- Resolves: #752774, #767795, #802198, #855863, #856975, #858266, #858754,
-           #858771, #858777, fdo#39386, fdo#54448, fdo#54522, fdo#54766

* Fri Jul 27 2012 Michal Schmidt <mschmidt@redhat.com> - 44-19
- Fix for broken fstab mounts in 44-18.
- Add scriptlets to migrate away from systemd-timedated-ntp.target.

* Tue Jul 24 2012 Michal Schmidt <mschmidt@redhat.com> - 44-18
- Backports from upstream:
- rework the handling of ntp services in timedated (#821813)
- rename systemd-debug-shell.service to debug-shell.service
- support modules-load= boot parameter
- "systemctl reset-failed" now resets the start rate limit
- systemctl can filter by load state
- parse BindsTo=
- bring back error reporting when stopping unknown units (#732874)
- many bugfixes (#817760, #835848, #767561, #839736, #841822, ...)

* Tue Jun 26 2012 Michal Schmidt <mschmidt@redhat.com> - 44-17
- Temporarily revert patch for #732874 until the syslog units are fixed.
- logind improvements (CanTTY, CanGraphical, 'closing' session state).
- Fix for auto-restart (#832039).
- Don't ship systemd-vconsole-setup on S390(x) (workaround for #834118).

* Wed Jun 20 2012 Michal Schmidt <mschmidt@redhat.com> - 44-16
- Add conflicts with syslog units that do unprotected 'systemctl stop' on
  a non-existent unit in their ExecStartPre.

* Tue Jun 19 2012 Michal Schmidt <mschmidt@redhat.com> - 44-15
- Apply timeouts to oneshot services (#761656)
- Report error when stopping an unknown unit (#732874)
- logind: more robust on VT-less systems (s390x) (#832210)
- journal: various fixes, expose cutoff times

* Thu Jun 14 2012 Michal Schmidt <mschmidt@redhat.com> - 44-14
- tmpfiles: correct SELinux context for char devices (#824059)
- systemctl: warn when stopping a triggerable unit (#714525)
- systemctl: clearer error message for missing [Install] (#817033)

* Wed Jun 13 2012 Michal Schmidt <mschmidt@redhat.com> - 44-13
- Patches from upstream
- Fixes to journald, logind, tmpfiles
- Documentation improvements, systemctl help
- New config options for systemd, journal
- Add systemd-readahead-analyze, systemd-debug-shell.service
- Start using Type=idle
- Fixes: #828007, #814424, #831132, #791098, #823815, fdo#50402, fdo#50671

* Tue May 22 2012 Michal Schmidt <mschmidt@redhat.com> - 44-12
- Fixes for auto-restart (#817968, fdo#45511)

* Mon May 21 2012 Michal Schmidt <mschmidt@redhat.com> - 44-11
- Fix weird "TIFIER=" messages in syslog (#823498)
- Revert ReleaseSession patch (#823485)
- Add more patches from upstream, notably:
  - Documentation= field support
  - RequiredBy= in [Install] support
  - configurable ulimit defaults
  - switch-root fixes

* Mon May 21 2012 Michal Schmidt <mschmidt@redhat.com> - 44-10
- Fix another cause of "Failed to issue method call" (#814966)
- minor systemd-delta updates

* Fri May 18 2012 Michal Schmidt <mschmidt@redhat.com> - 44-9
- Applied most of the patches from current upstream, while avoiding
  incompatible changes.
- NOT included:
  - systemadm removal
  - /media, /tmp tmpfs changes
  - systemd-*.conf config files rename
  - "service: schedule JOB_RESTART from SERVICE_AUTO_RESTART state"
    possible regression, https://bugs.freedesktop.org/show_bug.cgi?id=45511
  - udev merge
  - big LGPL relicensing patch
  - MountAuto=, SwapAuto= options removal
  - use of Type=idle for gettys by default
  - JobNew/JobRemoved dbus API change
- Fixes for reported BZs:
  - try-restart handling of units with scheduled jobs (#753586)
  - start requirement dependencies on "restart" (#802770)
  - systemd-tmpfiles did not preserve atime of subdirectories (#810257)
  - segfault in systemd-loginctl kill-session (#819142)
  - added shutdown inhibition support (#570594)
  - assertion failure in systemd-analyze (#701669)
  - bash-completion "Failed to issue method call" (#814966)
- Switched to using git for prep. Allows the use of renaming patches.

* Wed May 02 2012 Michal Schmidt <mschmidt@redhat.com> - 44-8
- Remove the "control" sub-cgroup patch. (#816842)
- Avoid #805942 by disabling the killing on START_PRE, START.

* Wed Apr 25 2012 Michal Schmidt <mschmidt@redhat.com> - 44-7
- Fixes for two bugs from the F17Blocker tracker:
  - Rescue shell on fsck errors (#798328)
  - Add systemd-timedated-ntp.target to avoid harcoded ntpd.service
    in timedated. Allows chrony to hook into it. (#815748)

* Tue Apr 24 2012 Michal Schmidt <mschmidt@redhat.com> - 44-6
- Revert most of the patches added in 44-5. F17 has 44-4 right now so let's
  try to minimize the risk of breakage before GA release. Apply only:
  - the fix for CVE-2012-1174
  - the PAGE_SIZE build fix
  - fix for a blocker bug (processes killed on libvirt restart, #805942)
  Fixes for less important bugs will be pushed post F17 GA.

* Fri Mar 30 2012 Michal Schmidt <mschmidt@redhat.com> - 44-5
- Post-v44 patches from upstream git, except the changes of /media, /tmp
  mountpoints and the gtk removal.

* Wed Mar 28 2012 Michal Schmidt <mschmidt@redhat.com> - 44-4
- Add triggers from Bill Nottingham to correct the damage done by
  the obsoleted systemd-units's preun scriptlet (#807457).

* Tue Mar 27 2012 Michal Schmidt <mschmidt@redhat.com> - 44-3.fc17.1
- Undo "Don't build the gtk parts anymore". It's for F>=18 only.

* Mon Mar 26 2012 Dennis Gilmore <dennis@ausil.us> - 44-3
- apply patch from upstream so we can build systemd on arm and ppc
- and likely the rest of the secondary arches

* Tue Mar 20 2012 Michal Schmidt <mschmidt@redhat.com> - 44-2
- Don't build the gtk parts anymore. They're moving into systemd-ui.
- Remove a dead patch file.

* Fri Mar 16 2012 Lennart Poettering <lpoetter@redhat.com> - 44-1
- New upstream release
- Closes #798760, #784921, #783134, #768523, #781735

* Mon Feb 27 2012 Dennis Gilmore <dennis@ausil.us> - 43-2
- don't conflict with fedora-release systemd never actually provided
- /etc/os-release so there is no actual conflict

* Wed Feb 15 2012 Lennart Poettering <lpoetter@redhat.com> - 43-1
- New upstream release
- Closes #789758, #790260, #790522

* Sat Feb 11 2012 Lennart Poettering <lpoetter@redhat.com> - 42-1
- New upstream release
- Save a bit of entropy during system installation (#789407)
- Don't own /etc/os-release anymore, leave that to fedora-release

* Thu Feb  9 2012 Adam Williamson <awilliam@redhat.com> - 41-2
- rebuild for fixed binutils

* Thu Feb  9 2012 Lennart Poettering <lpoetter@redhat.com> - 41-1
- New upstream release

* Tue Feb  7 2012 Lennart Poettering <lpoetter@redhat.com> - 40-1
- New upstream release

* Thu Jan 26 2012 Kay Sievers <kay@redhat.com> - 39-3
- provide /sbin/shutdown

* Wed Jan 25 2012 Harald Hoyer <harald@redhat.com> 39-2
- increment release

* Wed Jan 25 2012 Kay Sievers <kay@redhat.com> - 39-1.1
- install everything in /usr
  https://fedoraproject.org/wiki/Features/UsrMove

* Wed Jan 25 2012 Lennart Poettering <lpoetter@redhat.com> - 39-1
- New upstream release

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-6.git9fa2f41
- Update to a current git snapshot.
- Resolves: #781657

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-5
- Build against libgee06. Reenable gtk tools.
- Delete unused patches.
- Add easy building of git snapshots.
- Remove legacy spec file elements.
- Don't mention implicit BuildRequires.
- Configure with --disable-static.
- Merge -units into the main package.
- Move section 3 manpages to -devel.
- Fix unowned directory.
- Run ldconfig in scriptlets.
- Split systemd-analyze to a subpackage.

* Sat Jan 21 2012 Dan Horák <dan[at]danny.cz> - 38-4
- fix build on big-endians

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-3
- Disable building of gtk tools for now

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-2
- Fix a few (build) dependencies

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-1
- New upstream release

* Tue Nov 15 2011 Michal Schmidt <mschmidt@redhat.com> - 37-4
- Run authconfig if /etc/pam.d/system-auth is not a symlink.
- Resolves: #753160

* Wed Nov 02 2011 Michal Schmidt <mschmidt@redhat.com> - 37-3
- Fix remote-fs-pre.target and its ordering.
- Resolves: #749940

* Wed Oct 19 2011 Michal Schmidt <mschmidt@redhat.com> - 37-2
- A couple of fixes from upstream:
- Fix a regression in bash-completion reported in Bodhi.
- Fix a crash in isolating.
- Resolves: #717325

* Tue Oct 11 2011 Lennart Poettering <lpoetter@redhat.com> - 37-1
- New upstream release
- Resolves: #744726, #718464, #713567, #713707, #736756

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-5
- Undo the workaround. Kay says it does not belong in systemd.
- Unresolves: #741655

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-4
- Workaround for the crypto-on-lvm-on-crypto disk layout
- Resolves: #741655

* Sun Sep 25 2011 Michal Schmidt <mschmidt@redhat.com> - 36-3
- Revert an upstream patch that caused ordering cycles
- Resolves: #741078

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-2
- Add /etc/timezone to ghosted files

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-1
- New upstream release
- Resolves: #735013, #736360, #737047, #737509, #710487, #713384

* Thu Sep  1 2011 Lennart Poettering <lpoetter@redhat.com> - 35-1
- New upstream release
- Update post scripts
- Resolves: #726683, #713384, #698198, #722803, #727315, #729997, #733706, #734611

* Thu Aug 25 2011 Lennart Poettering <lpoetter@redhat.com> - 34-1
- New upstream release

* Fri Aug 19 2011 Harald Hoyer <harald@redhat.com> 33-2
- fix ABRT on service file reloading
- Resolves: rhbz#732020

* Wed Aug  3 2011 Lennart Poettering <lpoetter@redhat.com> - 33-1
- New upstream release

* Fri Jul 29 2011 Lennart Poettering <lpoetter@redhat.com> - 32-1
- New upstream release

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-2
- Fix access mode of modprobe file, restart logind after upgrade

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-1
- New upstream release

* Wed Jul 13 2011 Lennart Poettering <lpoetter@redhat.com> - 30-1
- New upstream release

* Thu Jun 16 2011 Lennart Poettering <lpoetter@redhat.com> - 29-1
- New upstream release

* Mon Jun 13 2011 Michal Schmidt <mschmidt@redhat.com> - 28-4
- Apply patches from current upstream.
- Fixes memory size detection on 32-bit with >4GB RAM (BZ712341)

* Wed Jun 08 2011 Michal Schmidt <mschmidt@redhat.com> - 28-3
- Apply patches from current upstream
- https://bugzilla.redhat.com/show_bug.cgi?id=709909
- https://bugzilla.redhat.com/show_bug.cgi?id=710839
- https://bugzilla.redhat.com/show_bug.cgi?id=711015

* Sat May 28 2011 Lennart Poettering <lpoetter@redhat.com> - 28-2
- Pull in nss-myhostname

* Thu May 26 2011 Lennart Poettering <lpoetter@redhat.com> - 28-1
- New upstream release

* Wed May 25 2011 Lennart Poettering <lpoetter@redhat.com> - 26-2
- Bugfix release
- https://bugzilla.redhat.com/show_bug.cgi?id=707507
- https://bugzilla.redhat.com/show_bug.cgi?id=707483
- https://bugzilla.redhat.com/show_bug.cgi?id=705427
- https://bugzilla.redhat.com/show_bug.cgi?id=707577

* Sat Apr 30 2011 Lennart Poettering <lpoetter@redhat.com> - 26-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=699394
- https://bugzilla.redhat.com/show_bug.cgi?id=698198
- https://bugzilla.redhat.com/show_bug.cgi?id=698674
- https://bugzilla.redhat.com/show_bug.cgi?id=699114
- https://bugzilla.redhat.com/show_bug.cgi?id=699128

* Thu Apr 21 2011 Lennart Poettering <lpoetter@redhat.com> - 25-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694788
- https://bugzilla.redhat.com/show_bug.cgi?id=694321
- https://bugzilla.redhat.com/show_bug.cgi?id=690253
- https://bugzilla.redhat.com/show_bug.cgi?id=688661
- https://bugzilla.redhat.com/show_bug.cgi?id=682662
- https://bugzilla.redhat.com/show_bug.cgi?id=678555
- https://bugzilla.redhat.com/show_bug.cgi?id=628004

* Wed Apr  6 2011 Lennart Poettering <lpoetter@redhat.com> - 24-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694079
- https://bugzilla.redhat.com/show_bug.cgi?id=693289
- https://bugzilla.redhat.com/show_bug.cgi?id=693274
- https://bugzilla.redhat.com/show_bug.cgi?id=693161

* Tue Apr  5 2011 Lennart Poettering <lpoetter@redhat.com> - 23-1
- New upstream release
- Include systemd-sysv-convert

* Fri Apr  1 2011 Lennart Poettering <lpoetter@redhat.com> - 22-1
- New upstream release

* Wed Mar 30 2011 Lennart Poettering <lpoetter@redhat.com> - 21-2
- The quota services are now pulled in by mount points, hence no need to enable them explicitly

* Tue Mar 29 2011 Lennart Poettering <lpoetter@redhat.com> - 21-1
- New upstream release

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 20-2
- Apply upstream patch to not send untranslated messages to plymouth

* Tue Mar  8 2011 Lennart Poettering <lpoetter@redhat.com> - 20-1
- New upstream release

* Tue Mar  1 2011 Lennart Poettering <lpoetter@redhat.com> - 19-1
- New upstream release

* Wed Feb 16 2011 Lennart Poettering <lpoetter@redhat.com> - 18-1
- New upstream release

* Mon Feb 14 2011 Bill Nottingham <notting@redhat.com> - 17-6
- bump upstart obsoletes (#676815)

* Wed Feb  9 2011 Tom Callaway <spot@fedoraproject.org> - 17-5
- add macros.systemd file for %%{_unitdir}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Lennart Poettering <lpoetter@redhat.com> - 17-3
- Fix popen() of systemctl, #674916

* Mon Feb  7 2011 Bill Nottingham <notting@redhat.com> - 17-2
- add epoch to readahead obsolete

* Sat Jan 22 2011 Lennart Poettering <lpoetter@redhat.com> - 17-1
- New upstream release

* Tue Jan 18 2011 Lennart Poettering <lpoetter@redhat.com> - 16-2
- Drop console.conf again, since it is not shipped in pamtmp.conf

* Sat Jan  8 2011 Lennart Poettering <lpoetter@redhat.com> - 16-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 15-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 14-1
- Upstream update
- Enable hwclock-load by default
- Obsolete readahead
- Enable /var/run and /var/lock on tmpfs

* Fri Nov 19 2010 Lennart Poettering <lpoetter@redhat.com> - 13-1
- new upstream release

* Wed Nov 17 2010 Bill Nottingham <notting@redhat.com> 12-3
- Fix clash

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-2
- Don't clash with initscripts for now, so that we don't break the builders

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-1
- New upstream release

* Fri Nov 12 2010 Matthias Clasen <mclasen@redhat.com> - 11-2
- Rebuild with newer vala, libnotify

* Thu Oct  7 2010 Lennart Poettering <lpoetter@redhat.com> - 11-1
- New upstream release

* Wed Sep 29 2010 Jesse Keating <jkeating@redhat.com> - 10-6
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Bill Nottingham <notting@redhat.com> - 10-5
- merge -sysvinit into main package

* Mon Sep 20 2010 Bill Nottingham <notting@redhat.com> - 10-4
- obsolete upstart-sysvinit too

* Fri Sep 17 2010 Bill Nottingham <notting@redhat.com> - 10-3
- Drop upstart requires

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-2
- Enable audit
- https://bugzilla.redhat.com/show_bug.cgi?id=633771

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=630401
- https://bugzilla.redhat.com/show_bug.cgi?id=630225
- https://bugzilla.redhat.com/show_bug.cgi?id=626966
- https://bugzilla.redhat.com/show_bug.cgi?id=623456

* Fri Sep  3 2010 Bill Nottingham <notting@redhat.com> - 9-3
- move fedora-specific units to initscripts; require newer version thereof

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-2
- Add missing tarball

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-1
- New upstream version
- Closes 501720, 614619, 621290, 626443, 626477, 627014, 627785, 628913

* Fri Aug 27 2010 Lennart Poettering <lpoetter@redhat.com> - 8-3
- Reexecute after installation, take ownership of /var/run/user
- https://bugzilla.redhat.com/show_bug.cgi?id=627457
- https://bugzilla.redhat.com/show_bug.cgi?id=627634

* Thu Aug 26 2010 Lennart Poettering <lpoetter@redhat.com> - 8-2
- Properly create default.target link

* Wed Aug 25 2010 Lennart Poettering <lpoetter@redhat.com> - 8-1
- New upstream release

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623561

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-2
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623430

* Tue Aug 10 2010 Lennart Poettering <lpoetter@redhat.com> - 7-1
- New upstream release

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-2
- properly hide output on package installation
- pull in coreutils during package installtion

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-1
- New upstream release
- Fixes #621200

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-2
- Add tarball

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-1
- Prepare release 5

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 4-4
- Add 'sysvinit-userspace' provide to -sysvinit package to fix upgrade/install (#618537)

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-3
- Add libselinux to build dependencies

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-2
- Use the right tarball

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-1
- New upstream release, and make default

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-3
- Used wrong tarball

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-2
- Own /cgroup jointly with libcgroup, since we don't dpend on it anymore

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-1
- New upstream release

* Fri Jul 9 2010 Lennart Poettering <lpoetter@redhat.com> - 2-0
- New upstream release

* Wed Jul 7 2010 Lennart Poettering <lpoetter@redhat.com> - 1-0
- First upstream release

* Tue Jun 29 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.7.20100629git4176e5
- New snapshot
- Split off -units package where other packages can depend on without pulling in the whole of systemd

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.6.20100622gita3723b
- Add missing libtool dependency.

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.5.20100622gita3723b
- Update snapshot

* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
