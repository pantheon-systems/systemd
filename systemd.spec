#global gitcommit 9fa2f41

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        44
Release:        12%{?gitcommit:.git%{gitcommit}}%{?dist}
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
