#global gitcommit e7aee75

# PIE is broken on s390 (#868839, #872148)
%ifnarch s390 s390x
%global _hardened_build 1
%endif

# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config

# Do not check .so files in the python_sitelib directory for provides.
%global __provides_exclude_from ^(%{python_sitearch}|%{python3_sitearch})/.*\\.so

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        208
Release:        30%{?gitcommit:.git%{gitcommit}}%{?dist}
# For a breakdown of the licensing, see README
License:        LGPLv2+ and MIT and GPLv2+
Summary:        A System and Service Manager

%if %{defined gitcommit}
# Snapshot tarball can be created using: ./make-git-shapshot.sh [gitcommit]
Source0:        %{name}-git%{gitcommit}.tar.xz
%else
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
%endif
# Fedora's default preset policy
Source1:        90-default.preset
Source7:        99-default-disable.preset
Source5:        85-display-manager.preset
# Stop-gap, just to ensure things work fine with rsyslog without having to change the package right-away
Source4:        listen.conf
# Prevent accidental removal of the systemd package
Source6:        yum-protect-systemd.conf

# Patch series is available from http://cgit.freedesktop.org/systemd/systemd-stable/log/?h=v208-stable
# GIT_DIR=~/src/systemd/.git git format-patch-ab -M -N --no-signature v208..v208-stable
# i=1; for p in 0*patch;do printf "Patch%03d:       %s\n" $i $p; ((i++));done
Patch001:       0001-acpi-fptd-fix-memory-leak-in-acpi_get_boot_usec.patch
Patch002:       0002-fix-lingering-references-to-var-lib-backlight-random.patch
Patch003:       0003-acpi-make-sure-we-never-free-an-uninitialized-pointe.patch
Patch004:       0004-systemctl-fix-name-mangling-for-sysv-units.patch
Patch005:       0005-cryptsetup-fix-OOM-handling-when-parsing-mount-optio.patch
Patch006:       0006-journald-add-missing-error-check.patch
Patch007:       0007-bus-fix-potentially-uninitialized-memory-access.patch
Patch008:       0008-dbus-fix-return-value-of-dispatch_rqueue.patch
Patch009:       0009-modules-load-fix-error-handling.patch
Patch010:       0010-efi-never-call-qsort-on-potentially-NULL-arrays.patch
Patch011:       0011-strv-don-t-access-potentially-NULL-string-arrays.patch
Patch012:       0012-mkdir-pass-a-proper-function-pointer-to-mkdir_safe_i.patch
Patch013:       0013-tmpfiles.d-include-setgid-perms-for-run-log-journal.patch
Patch014:       0014-execute.c-always-set-SHELL.patch
Patch015:       0015-man-Improve-the-description-of-parameter-X-in-tmpfil.patch
Patch016:       0016-execute-more-debugging-messages.patch
Patch017:       0017-gpt-auto-generator-exit-immediately-if-in-container.patch
Patch018:       0018-systemd-order-remote-mounts-from-mountinfo-before-re.patch
Patch019:       0019-manager-when-verifying-whether-clients-may-change-en.patch
Patch020:       0020-logind-fix-bus-introspection-data-for-TakeControl.patch
Patch021:       0021-mount-check-for-NULL-before-reading-pm-what.patch
Patch022:       0022-core-do-not-add-what-to-RequiresMountsFor-for-networ.patch
Patch023:       0023-utf8-fix-utf8_is_printable.patch
Patch024:       0024-shared-util-fix-off-by-one-error-in-tag_to_udev_node.patch
Patch025:       0025-systemd-serialize-deserialize-forbid_restart-value.patch
Patch026:       0026-core-unify-the-way-we-denote-serialization-attribute.patch
Patch027:       0027-journald-fix-minor-memory-leak.patch
Patch028:       0028-keymap-Fix-Samsung-900X-34-C.patch
Patch029:       0029-do-not-accept-garbage-from-acpi-firmware-performance.patch
Patch030:       0030-journald-remove-rotated-file-from-hashmap-when-rotat.patch
Patch031:       0031-login-fix-invalid-free-in-sd_session_get_vt.patch
Patch032:       0032-login-make-sd_session_get_vt-actually-work.patch
Patch033:       0033-udevadm.xml-document-resolve-names-option-for-test.patch
Patch034:       0034-Never-call-qsort-on-potentially-NULL-arrays.patch
Patch035:       0035-dbus-common-avoid-leak-in-error-path.patch
Patch036:       0036-drop-ins-check-return-value.patch
Patch037:       0037-Make-sure-that-we-don-t-dereference-NULL.patch
Patch038:       0038-gitignore-ignore-clang-analyze-output.patch
Patch039:       0039-man-add-more-markup-to-udevadm-8.patch
Patch040:       0040-shared-util-Fix-glob_extend-argument.patch
Patch041:       0041-Fix-bad-assert-in-show_pid_array.patch
Patch042:       0042-Fix-for-SIGSEGV-in-systemd-bootchart-on-short-living.patch
Patch043:       0043-man-document-the-b-special-boot-option.patch
Patch044:       0044-logind-allow-unprivileged-session-device-access.patch
Patch045:       0045-rules-expose-loop-block-devices-to-systemd.patch
Patch046:       0046-rules-don-t-limit-some-of-the-rules-to-the-add-actio.patch
Patch047:       0047-tmpfiles-log-unaccessible-FUSE-mount-points-only-as-.patch
Patch048:       0048-hwdb-update.patch
Patch049:       0049-rules-remove-pointless-MODE-settings.patch
Patch050:       0050-analyze-set-white-backgound.patch
Patch051:       0051-shell-completion-dump-has-moved-to-systemd-analyze.patch
Patch052:       0052-systemd-use-unit-name-in-PrivateTmp-directories.patch
Patch053:       0053-catalog-remove-links-to-non-existent-wiki-pages.patch
Patch054:       0054-journalctl-add-list-boots-to-show-boot-IDs-and-times.patch
Patch055:       0055-udev-builtin-path_id-add-support-for-bcma-bus.patch
Patch056:       0056-udev-ata_id-log-faling-ioctls-as-debug.patch
Patch057:       0057-libudev-default-log_priority-to-INFO.patch
Patch058:       0058-nspawn-only-pass-in-slice-setting-if-it-is-set.patch
Patch059:       0059-zsh-completion-add-systemd-run.patch
Patch060:       0060-man-explain-NAME-in-systemctl-man-page.patch
Patch061:       0061-virt-move-caching-of-virtualization-check-results-in.patch
Patch062:       0062-systemctl-fix-typo-in-help-text.patch
Patch063:       0063-analyze-plot-place-the-text-on-the-side-with-most-sp.patch
Patch064:       0064-detect_virtualization-returns-NULL-pass-empty-string.patch
Patch065:       0065-rules-load-path_id-on-DRM-devices.patch
Patch066:       0066-rules-simply-60-drm.rules.patch
Patch067:       0067-udev-builtin-keyboard-Fix-large-scan-codes-on-32-bit.patch
Patch068:       0068-nspawn-log-out-of-memory-errors.patch
Patch069:       0069-Configurable-Timeouts-Restarts-default-values.patch
Patch070:       0070-man-fix-typo.patch
Patch071:       0071-man-do-not-use-term-in-para.patch
Patch072:       0072-cgroup-run-PID-1-in-the-root-cgroup.patch
Patch073:       0073-shutdown-trim-the-cgroup-tree-on-loop-iteration.patch
Patch074:       0074-nspawn-split-out-pty-forwaring-logic-into-ptyfwd.c.patch
Patch075:       0075-nspawn-explicitly-terminate-machines-when-we-exit-ns.patch
Patch076:       0076-run-support-system-to-match-other-commands-even-if-r.patch
Patch077:       0077-acpi-fpdt-break-on-zero-or-negative-length-read.patch
Patch078:       0078-man-add-rationale-into-systemd-halt-8.patch
Patch079:       0079-systemd-python-convert-keyword-value-to-string.patch
Patch080:       0080-systemctl-make-LOAD-column-width-dynamic.patch
Patch081:       0081-Make-hibernation-test-work-for-swap-files.patch
Patch082:       0082-man-add-docs-for-sd_is_special-and-some-man-page-sym.patch
Patch083:       0083-systemctl-return-r-instead-of-always-returning-0.patch
Patch084:       0084-journal-fix-minor-memory-leak.patch
Patch085:       0085-manager-configurable-StartLimit-default-values.patch
Patch086:       0086-man-units-fix-installation-of-systemd-nspawn-.servic.patch
Patch087:       0087-systemd-fix-memory-leak-in-cgroup-code.patch
Patch088:       0088-button-don-t-exit-if-we-cannot-handle-a-button-press.patch
Patch089:       0089-timer-properly-format-relative-timestamps-in-the-fut.patch
Patch090:       0090-timer-consider-usec_t-1-an-invalid-timestamp.patch
Patch091:       0091-udev-usb_id-remove-obsoleted-bInterfaceSubClass-5-ma.patch
Patch092:       0092-Add-support-for-saving-restoring-keyboard-backlights.patch
Patch093:       0093-static-nodes-don-t-call-mkdir.patch
Patch094:       0094-Fix-kmod-error-message-to-have-correct-version-requi.patch
Patch095:       0095-systemd-python-fix-booted-and-add-two-functions-to-d.patch
Patch096:       0096-activate-mention-E-in-the-help-text.patch
Patch097:       0097-activate-fix-crash-when-s-is-passed.patch
Patch098:       0098-journal-timestamp-support-on-console-messages.patch
Patch099:       0099-man-add-bootctl-8.patch
Patch100:       0100-zsh-completion-add-bootctl.patch
Patch101:       0101-Resolve-dev-console-to-the-active-tty-instead-of-jus.patch
Patch102:       0102-Only-disable-output-on-console-during-boot-if-needed.patch
Patch103:       0103-Fix-possible-lack-of-status-messages-on-shutdown-reb.patch
Patch104:       0104-fsck-modernization.patch
Patch105:       0105-Introduce-udev-object-cleanup-functions.patch
Patch106:       0106-util-allow-trailing-semicolons-on-define_trivial_cle.patch
Patch107:       0107-fsck-fstab-generator-be-lenient-about-missing-fsck.-.patch
Patch108:       0108-fstab-generator-use-RequiresOverridable-for-fsck-uni.patch
Patch109:       0109-bash-completion-journalctl-file.patch
Patch110:       0110-random-seed-improve-debugging-messages-a-bit.patch
Patch111:       0111-Fix-RemainAfterExit-services-keeping-a-hold-on-conso.patch
Patch112:       0112-tmpfiles-adjust-excludes-for-the-new-per-service-pri.patch
Patch113:       0113-core-socket-fix-SO_REUSEPORT.patch
Patch114:       0114-localed-match-converted-keymaps-before-legacy.patch
Patch115:       0115-keymap-Add-Toshiba-Satellite-U940.patch
Patch116:       0116-calendar-support-yearly-and-annually-names-the-same-.patch
Patch117:       0117-hashmap-be-a-bit-more-conservative-with-pre-allocati.patch
Patch118:       0118-manager-don-t-do-plymouth-in-a-container.patch
Patch119:       0119-nspawn-add-new-drop-capability-switch.patch
Patch120:       0120-valgrind-make-running-PID-1-in-valgrind-useful.patch
Patch121:       0121-efi-boot-generator-don-t-mount-boot-eagerly.patch
Patch122:       0122-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch123:       0123-journal-when-appending-to-journal-file-allocate-larg.patch
Patch124:       0124-journal-make-table-const.patch
Patch125:       0125-journald-keep-statistics-on-how-of-we-hit-miss-the-m.patch
Patch126:       0126-journal-optimize-bisection-logic-a-bit-by-caching-th.patch
Patch127:       0127-journal-fix-iteration-when-we-go-backwards-from-the-.patch
Patch128:       0128-journal-allow-journal_file_copy_entry-to-work-on-non.patch
Patch129:       0129-journal-simplify-pre-allocation-logic.patch
Patch130:       0130-journald-mention-how-long-we-needed-to-flush-to-var-.patch
Patch131:       0131-automount-log-info-about-triggering-process.patch
Patch132:       0132-virt-split-detect_vm-into-separate-functions.patch
Patch133:       0133-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch134:       0134-sysfs-show.c-return-negative-error.patch
Patch135:       0135-util.c-check-if-return-value-from-ttyname_r-is-0-ins.patch
Patch136:       0136-docs-remove-unneeded-the-s-in-gudev-docs.patch
Patch137:       0137-man-explicitly-say-when-multiple-units-can-be-specif.patch
Patch138:       0138-systemd-treat-reload-failure-as-failure.patch
Patch139:       0139-journal-fail-silently-in-sd_j_sendv-if-journal-is-un.patch
Patch140:       0140-systemd-add-a-start-job-for-all-units-specified-with.patch
Patch141:       0141-core-device-ignore-SYSTEMD_WANTS-in-user-mode.patch
Patch142:       0142-Fix-memory-leak-in-stdout-journal-streams.patch
Patch143:       0143-man-document-is-enabled-output.patch
Patch144:       0144-hostnamed-avoid-using-NULL-in-error-path.patch
Patch145:       0145-logind-use-correct-who-enum-values-with-KillUnit.patch
Patch146:       0146-Revert-systemd-add-a-start-job-for-all-units-specifi.patch
Patch147:       0147-core-do-not-segfault-if-swap-activity-happens-when-p.patch
Patch148:       0148-kernel-install-add-h-help.patch
Patch149:       0149-kernel-install-fix-help-output.patch
Patch150:       0150-man-improve-wording-and-comma-usage-in-systemd.journ.patch
Patch151:       0151-drop-several-entries-from-kbd-model-map-whose-kbd-la.patch
Patch152:       0152-correct-name-of-Tajik-kbd-layout-in-kbd-model-map.patch
Patch153:       0153-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch154:       0154-Ensure-unit-is-journaled-for-short-lived-or-oneshot-.patch
Patch155:       0155-libudev-hwdb-use-libudev-not-systemd-logging.patch
Patch156:       0156-core-manager-remove-infinite-loop.patch
Patch157:       0157-util-check-for-overflow-in-greedy_realloc.patch
Patch158:       0158-journald-use-a-bit-more-cleanup-magic.patch
Patch159:       0159-journald-malloc-less-when-streaming-messages.patch
Patch160:       0160-activate-clean-up-inherited-descriptors.patch
Patch161:       0161-man-explain-in-more-detail-how-SYSTEMD_READY-influen.patch
Patch162:       0162-units-don-t-run-readahead-done-timers-in-containers.patch
Patch163:       0163-test-fileio-replace-mktemp-with-mkstemp-to-avoid-war.patch
Patch164:       0164-journal-pipe-journalctl-help-output-into-a-pager.patch
Patch165:       0165-nspawn-complain-and-continue-if-machine-has-same-id.patch
Patch166:       0166-man-beef-up-ExecStart-description.patch
Patch167:       0167-man-remove-advice-to-avoid-setting-the-same-var-more.patch
Patch168:       0168-systemctl-add-the-plain-option-to-the-help-message.patch
Patch169:       0169-Fix-a-few-resource-leaks-in-error-paths.patch
Patch170:       0170-Fix-a-few-signed-unsigned-format-string-issues.patch
Patch171:       0171-util-try-harder-to-increase-the-send-recv-buffers-of.patch
Patch172:       0172-execute-also-set-SO_SNDBUF-when-spawning-a-service-w.patch
Patch173:       0173-journal-file-protect-against-alloca-0.patch
Patch174:       0174-man-describe-journalctl-show-cursor.patch
Patch175:       0175-journal-fix-against-theoretical-undefined-behavior.patch
Patch176:       0176-journald-downgrade-warning-message-when-dev-kmsg-doe.patch
Patch177:       0177-journal-file.c-remove-redundant-assignment-of-variab.patch
Patch178:       0178-login-Don-t-stop-a-running-user-manager-from-garbage.patch
Patch179:       0179-libudev-devices-received-from-udev-are-always-initia.patch
Patch180:       0180-log-don-t-reopen-dev-console-each-time-we-call-log_o.patch
Patch181:       0181-log-when-we-log-to-dev-console-and-got-disconnected-.patch
Patch182:       0182-loginctl-when-showing-device-tree-of-seats-with-no-d.patch
Patch183:       0183-man-be-more-explicit-about-option-arguments-that-tak.patch
Patch184:       0184-man-add-DOI-for-refereed-article-on-Forward-Secure-S.patch
Patch185:       0185-journalctl-zsh-completion-fix-several-issues-in-help.patch
Patch186:       0186-keymap-Refactor-Acer-tables.patch
Patch187:       0187-logging-reduce-send-timeout-to-something-more-sensib.patch
Patch188:       0188-DEFAULT_PATH_SPLIT_USR-macro.patch
Patch189:       0189-fstab-generator-Do-not-try-to-fsck-non-devices.patch
Patch190:       0190-logind-remove-dead-variable.patch
Patch191:       0191-hwdb-update.patch
Patch192:       0192-delta-replace-readdir_r-with-readdir.patch
Patch193:       0193-delta-fix-delta-for-drop-ins.patch
Patch194:       0194-delta-if-prefix-is-specified-only-show-overrides-the.patch
Patch195:       0195-log-log_error-and-friends-add-a-newline-after-each-l.patch
Patch196:       0196-man-units-tmpfiles.d-5-cleanup.patch
Patch197:       0197-tmpfiles-introduce-the-concept-of-unsafe-operations.patch
Patch198:       0198-sleep-config-fix-useless-check-for-swapfile-type.patch
Patch199:       0199-journalctl-make-sure-b-foobar-cannot-be-misunderstoo.patch
Patch200:       0200-man-resolve-word-omissions.patch
Patch201:       0201-man-improvements-to-comma-placement.patch
Patch202:       0202-man-grammar-and-wording-improvements.patch
Patch203:       0203-man-document-fail-nofail-auto-noauto.patch
Patch204:       0204-man-fix-description-of-is-enabled-returned-value.patch
Patch205:       0205-man-fix-Type-reference.patch
Patch206:       0206-man-fix-Type-reference-v2.patch
Patch207:       0207-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch208:       0208-man-add-a-note-about-propagating-signals.patch
Patch209:       0209-man-include-autoconf-snippet-in-daemon-7.patch
Patch210:       0210-systemd-python-fix-setting-of-exception-codes.patch
Patch211:       0211-systemd-python-fix-listen_fds-under-Python-2.patch
Patch212:       0212-man-expand-on-some-more-subtle-points-in-systemd.soc.patch
Patch213:       0213-tmpfiles-rename-unsafe-to-boot.patch
Patch214:       0214-sleep-config-Dereference-pointer-before-check-for-NU.patch
Patch215:       0215-sleep-config-fix-double-free.patch
Patch216:       0216-rules-drivers-do-not-reset-RUN-list.patch
Patch217:       0217-core-manager-print-info-about-interesting-signals.patch
Patch218:       0218-core-service-check-if-mainpid-matches-only-if-it-is-.patch
Patch219:       0219-man-typo-fix.patch
Patch220:       0220-swap-remove-if-else-with-the-same-data-path.patch
Patch221:       0221-hwdb-update.patch
Patch222:       0222-journal-Add-missing-byte-order-conversions.patch
Patch223:       0223-hwdb-change-key-mappings-for-Samsung-90X3A.patch
Patch224:       0224-hwdb-add-Samsung-700G.patch
Patch225:       0225-hwdb-remove-duplicate-entry-for-Samsung-700Z.patch
Patch226:       0226-hwdb-fix-match-for-Thinkpad-X201-tablet.patch
Patch227:       0227-keymap-Recognize-different-Toshiba-Satellite-capital.patch
Patch228:       0228-sleep.c-fix-typo.patch
Patch229:       0229-delta-ensure-that-d_type-will-be-set-on-every-fs.patch
Patch230:       0230-tmpfiles-don-t-allow-label_fix-to-print-ENOENT-when-.patch
Patch231:       0231-man-mention-which-variables-will-be-expanded-in-Exec.patch
Patch232:       0232-hwdb-Add-support-for-Toshiba-Satellite-P75-A7200-key.patch
Patch233:       0233-journal-fix-access-to-munmapped-memory-in-sd_journal.patch
Patch234:       0234-gpt-auto-generator-skip-nonexistent-devices.patch
Patch235:       0235-gpt-auto-generator-use-EBADSLT-code-when-unable-to-d.patch
Patch236:       0236-journald-do-not-free-space-when-disk-space-runs-low.patch
Patch237:       0237-man-add-busctl-1.patch
Patch238:       0238-journalctl-flip-to-full-by-default.patch
Patch239:       0239-coredumpctl-in-case-of-error-free-pattern-after-prin.patch
Patch240:       0240-shell-completion-remove-load-from-systemctl.patch
Patch241:       0241-units-drop-Install-section-from-multi-user.target-an.patch
Patch242:       0242-systemctl-skip-native-unit-file-handling-if-sysv-fil.patch
Patch243:       0243-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch244:       0244-udev-static_node-do-not-exit-rule-after-first-static.patch
Patch245:       0245-cryptsetup-Support-key-slot-option.patch
Patch246:       0246-pam_systemd-Ignore-vtnr-when-seat-seat0.patch
Patch247:       0247-keymap-Add-HP-Chromebook-14-Falco.patch
Patch248:       0248-keymap-Add-release-quirk-for-Acer-AOA-switchvideomod.patch
Patch249:       0249-keymap-Add-Sony-Vaio-VGN-FW250.patch
Patch250:       0250-keymap-Add-Toshiba-EQUIUM.patch
Patch251:       0251-tmpfiles-fix-memory-leak-of-exclude_prefixes.patch
Patch252:       0252-analyze-fix-plot-issues-when-using-gummiboot.patch
Patch253:       0253-udev-add-zram-to-the-list-of-devices-inappropriate-f.patch
Patch254:       0254-bash-completion-fix-completion-of-complete-verbs.patch
Patch255:       0255-shell-completion-fix-completion-of-localectl-set-loc.patch
Patch256:       0256-zsh-completions-kernel-install-only-show-existing-ke.patch
Patch257:       0257-core-fix-crashes-if-locale.conf-contains-invalid-utf.patch
Patch258:       0258-core-do-not-print-invalid-utf-8-in-error-messages.patch
Patch259:       0259-cryptsetup-generator-auto-add-deps-for-device-as-pas.patch
Patch260:       0260-man-fix-reference-in-systemd-inhibit-1.patch
Patch261:       0261-man-fix-another-reference-in-systemd-inhibit-1.patch
Patch262:       0262-fstab-generator-Create-fsck-root-symlink-with-correc.patch
Patch263:       0263-efi-fix-Undefined-reference-efi_loader_get_boot_usec.patch
Patch264:       0264-core-make-StopWhenUnneeded-work-in-conjunction-with-.patch
Patch265:       0265-man-always-place-programlisting-and-programlisting-i.patch
Patch266:       0266-Temporary-work-around-for-slow-shutdown-due-to-unter.patch
Patch267:       0267-pam-module-fix-warning-about-ignoring-vtnr.patch
Patch268:       0268-pam_systemd-do-not-set-XDG_RUNTIME_DIR-if-the-sessio.patch
Patch269:       0269-core-do-not-segfault-if-proc-swaps-cannot-be-opened.patch
Patch270:       0270-Revert-login-Don-t-stop-a-running-user-manager-from-.patch
Patch271:       0271-Revert-journalctl-flip-to-full-by-default.patch
Patch272:       0272-util-fix-handling-of-trailing-whitespace-in-split_qu.patch
Patch273:       0273-udev-net_id-Introduce-predictable-network-names-for-.patch
Patch274:       0274-utils-silence-the-compiler-warning.patch
Patch275:       0275-fix-SELinux-check-for-transient-units.patch
Patch276:       0276-s390-getty-generator-initialize-essential-system-ter.patch
Patch277:       0277-pam-use-correct-log-level.patch
Patch278:       0278-nspawn-if-we-don-t-find-bash-try-sh.patch
Patch279:       0279-units-systemd-logind-fails-hard-without-dbus.patch
Patch280:       0280-man-fix-grammatical-errors-and-other-formatting-issu.patch
Patch281:       0281-man-replace-STDOUT-with-standard-output-etc.patch
Patch282:       0282-man-use-spaces-instead-of-tabs.patch
Patch283:       0283-macro-add-a-macro-to-test-whether-a-value-is-in-a-sp.patch
Patch284:       0284-core-fix-property-changes-in-transient-units.patch
Patch285:       0285-core-more-exact-test-on-the-procfs-special-string-de.patch
Patch286:       0286-doc-update-punctuation.patch
Patch287:       0287-doc-resolve-missing-extraneous-words-or-inappropriat.patch
Patch288:       0288-doc-choose-different-words-to-improve-clarity.patch
Patch289:       0289-doc-properly-use-XML-entities.patch
Patch290:       0290-man-machinectl-there-is-no-command-kill-machine.patch
Patch291:       0291-load-modules-properly-return-a-failing-error-code-if.patch
Patch292:       0292-machinectl-add-bash-completion.patch
Patch293:       0293-delta-add-bash-completion.patch
Patch294:       0294-man-document-MAINPID.patch
Patch295:       0295-man-busctl-typo-fix.patch
Patch296:       0296-journal-don-t-clobber-return-parameters-of-sd_journa.patch
Patch297:       0297-udev-make-sure-we-always-return-a-valid-error-code-i.patch
Patch298:       0298-bootctl-add-bash-completion.patch
Patch299:       0299-selinux-Don-t-attempt-to-load-policy-in-initramfs-if.patch
Patch300:       0300-man-there-is-no-ExecStopPre-for-service-units.patch
Patch301:       0301-man-document-that-per-interface-sysctl-variables-are.patch
Patch302:       0302-journal-downgrade-vaccuum-message-to-debug-level.patch
Patch303:       0303-core-gc-half-created-stub-units.patch
Patch304:       0304-getty-generator-verify-ttys-before-we-make-use-of-th.patch
Patch305:       0305-units-serial-getty-.service-add-Install-section.patch
Patch306:       0306-README-document-that-var-run-must-be-a-symlink-run.patch
Patch307:       0307-Use-var-run-dbus-system_bus_socket-for-the-D-Bus-soc.patch
Patch308:       0308-mount-don-t-send-out-PropertiesChanged-message-if-ac.patch
Patch309:       0309-mount-don-t-fire-PropertiesChanged-signals-for-mount.patch
Patch310:       0310-logs-show-fix-corrupt-output-with-empty-messages.patch
Patch311:       0311-journalctl-refuse-extra-arguments-with-verify-and-si.patch
Patch312:       0312-cdrom_id-use-the-old-MMC-fallback.patch
Patch313:       0313-udev-rules-setup-tty-permissions-and-group-for-sclp_.patch
Patch314:       0314-bash-add-completion-for-systemd-nspawn.patch
Patch315:       0315-add-bash-completion-for-systemd-cgls.patch
Patch316:       0316-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch317:       0317-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch318:       0318-Allow-fractional-parts-in-disk-sizes.patch
Patch319:       0319-add-bash-completion-for-systemd-cgtop.patch
Patch320:       0320-execute-free-directory-path-if-we-fail-to-remove-it-.patch
Patch321:       0321-add-bash-completion-for-systemd-detect-virt.patch
Patch322:       0322-Do-not-print-invalid-UTF-8-in-error-messages.patch
Patch323:       0323-add-bash-completion-for-systemd-cat.patch
Patch324:       0324-journal-assume-that-next-entry-is-after-previous-ent.patch
Patch325:       0325-journal-forget-file-after-encountering-an-error.patch
Patch326:       0326-logind-ignore-failing-close-on-session-devices.patch
Patch327:       0327-core-introduce-new-stop-protocol-for-unit-scopes.patch
Patch328:       0328-core-watch-SIGCHLD-more-closely-to-track-processes-o.patch
Patch329:       0329-logind-rework-session-shutdown-logic.patch
Patch330:       0330-logind-order-all-scopes-after-both-systemd-logind.se.patch
Patch331:       0331-logind-given-that-we-can-now-relatively-safely-shutd.patch
Patch332:       0332-logind-fix-reference-to-systemd-user-sessions.servic.patch
Patch333:       0333-logind-add-forgotten-call-to-user_send_changed.patch
Patch334:       0334-logind-save-session-after-setting-the-stopping-flag.patch
Patch335:       0335-logind-save-user-state-after-stopping-the-session.patch
Patch336:       0336-logind-initialize-timer_fd.patch
Patch337:       0337-logind-pass-pointer-to-User-object-to-user_save.patch
Patch338:       0338-core-allow-PIDs-to-be-watched-by-two-units-at-the-sa.patch
Patch339:       0339-core-correctly-unregister-PIDs-from-PID-hashtables.patch
Patch340:       0340-logind-uninitialized-timer_fd-is-set-to-1.patch
Patch341:       0341-logind-add-forgotten-return-statement.patch
Patch342:       0342-core-fix-detection-of-dead-processes.patch
Patch343:       0343-Fix-prototype-of-get_process_state.patch
Patch344:       0344-core-check-for-return-value-from-get_process_state.patch
Patch345:       0345-man-update-link-to-LSB.patch
Patch346:       0346-man-systemd-bootchart-fix-spacing-in-command.patch
Patch347:       0347-man-add-missing-comma.patch
Patch348:       0348-build-sys-Don-t-distribute-generated-udev-rule.patch
Patch349:       0349-units-Do-not-unescape-instance-name-in-systemd-backl.patch
Patch350:       0350-util-add-timeout-to-generator-execution.patch
Patch351:       0351-input_id-Recognize-buttonless-joystick-types.patch
Patch352:       0352-logind-fix-policykit-checks.patch
Patch353:       0353-nspawn-don-t-try-mknod-of-dev-console-with-the-corre.patch
Patch354:       0354-build-sys-Find-the-tools-for-users-with-no-sbin-usr-.patch
Patch355:       0355-rules-mark-loop-device-as-SYSTEMD_READY-0-if-no-file.patch
Patch356:       0356-man-multiple-sleep-modes-are-to-be-separated-by-whit.patch
Patch357:       0357-man-fix-description-of-systemctl-after-before.patch
Patch358:       0358-udev-properly-detect-reference-to-unexisting-part-of.patch
Patch359:       0359-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch360:       0360-gpt-auto-generator-don-t-return-OOM-on-parentless-de.patch
Patch361:       0361-man-improve-wording-of-systemctl-s-after-before.patch
Patch362:       0362-cgroup-it-s-not-OK-to-invoke-alloca-in-loops.patch
Patch363:       0363-hwdb-update.patch
Patch364:       0364-core-don-t-try-to-relabel-mounts-before-we-loaded-th.patch
Patch365:       0365-man-explain-that-the-journal-field-SYSLOG_IDENTIFIER.patch
Patch366:       0366-man-be-more-specific-when-EnvironmentFile-is-read.patch
Patch367:       0367-systemctl-kill-mode-is-long-long-gone-don-t-mention-.patch
Patch368:       0368-systemctl-add-more-verbose-explanation-of-kill-who-a.patch
Patch369:       0369-ask-password-when-the-user-types-a-overly-long-passw.patch
Patch370:       0370-util-consider-both-fuse.glusterfs-and-glusterfs-netw.patch
Patch371:       0371-core-do-not-read-system-boot-timestamps-in-systemd-u.patch
Patch372:       0372-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch373:       0373-Add-hwdb-entry-for-Samsung-Series-7-Ultra.patch
Patch374:       0374-udev-do-not-export-static-node-tags-for-non-existing.patch
Patch375:       0375-journalctl-free-arg_file-on-exit.patch
Patch376:       0376-journal-fix-export-of-messages-containing-newlines.patch
Patch377:       0377-tty-ask-password-agent-return-negative-errno.patch
Patch378:       0378-systemd-python-use-.hex-instead-of-.get_hex.patch
Patch379:       0379-reduce-the-amount-of-messages-logged-to-dev-kmsg-whe.patch
Patch380:       0380-journal-cleanup-up-error-handling-in-update_catalog.patch
Patch381:       0381-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch382:       0382-bash-completion-fix-__get_startable_units.patch
Patch383:       0383-hwdb-update.patch
Patch384:       0384-hwdb-PCI-include-primary-model-string-in-subsystem-m.patch
Patch385:       0385-sysctl-replaces-some-slashes-with-dots.patch
Patch386:       0386-man-document-relationship-between-RequiresMountsFor-.patch
Patch387:       0387-install-create_symlink-check-unlink-return-value.patch
Patch388:       0388-delta-do-not-use-unicode-chars-in-C-locale.patch
Patch389:       0389-core-print-debug-instead-of-error-message.patch
Patch390:       0390-tmpfiles-fix-permissions-on-new-journal-files.patch
Patch391:       0391-implement-a-union-to-pad-out-file_handle.patch
Patch392:       0392-analyze-fix-plot-with-bad-y-size.patch
Patch393:       0393-util-make-sure-all-our-name_to_handle_at-code-makes-.patch
Patch394:       0394-Fix-keysize-handling-in-cryptsetup-bits-vs.-bytes.patch
Patch395:       0395-udev-increase-the-size-of-RESULT-buffer.patch
Patch396:       0396-job-add-waiting-jobs-to-run-queue-in-unit_coldplug.patch
Patch397:       0397-machine-id-only-look-into-KVM-uuid-when-we-are-not-r.patch
Patch398:       0398-hwdb-update.patch
Patch399:       0399-core-check-the-right-variable-for-failed-open.patch
Patch400:       0400-man-sd_journal_send-does-nothing-when-journald-is-no.patch
Patch401:       0401-core-sysvcompat-network-should-be-equivalent-to-netw.patch
Patch402:       0402-udev-do-not-skip-the-execution-of-RUN-when-renaming-.patch
Patch403:       0403-udev-avoid-use-of-uninitialized-err.patch
Patch404:       0404-shared-install-do-not-prefix-created-symlink-with-ro.patch
Patch405:       0405-shared-include-root-when-canonicalizing-conf-paths.patch
Patch406:       0406-Make-systemctl-root-look-for-files-in-the-proper-pla.patch
Patch407:       0407-util-replace-close_nointr_nofail-by-a-more-useful-sa.patch
Patch408:       0408-async-add-asynchronous-close-call.patch
Patch409:       0409-core-close-socket-fds-asynchronously.patch
Patch410:       0410-logind-bring-polkit-policy-for-hibernate-in-line-wit.patch
Patch411:       0411-unit.c-Move-code-around-to-easy-cherrypicking.patch
Patch412:       0412-core-make-sure-to-serialize-jobs-for-all-units.patch
Patch413:       0413-man-clarify-that-the-ExecReload-command-should-be-sy.patch
Patch414:       0414-man-readahead-fix-cmdline-switch-inconsistency-betwe.patch
Patch415:       0415-build-sys-at-configure-check-for-verifying-that-ln-s.patch
Patch416:       0416-man-update-journald-rate-limit-defaults.patch
Patch417:       0417-nspawn-properly-format-container_uuid-in-UUID-format.patch
Patch418:       0418-core-reindent-selinux-ima-smack-setup.c.patch
Patch419:       0419-core-let-selinux_setup-load-policy-more-than-once.patch
Patch420:       0420-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch421:       0421-hwdb-update.patch
Patch422:       0422-nspawn-allow-to-bind-mount-journal-on-top-of-a-non-e.patch
Patch423:       0423-nspawn-restore-journal-directory-is-empty-check.patch
Patch424:       0424-machine-escape-fields-we-store-in-run-so-that-they-c.patch
Patch425:       0425-logind-also-escape-external-data-when-saving-to-run.patch
Patch426:       0426-man-drop-reference-to-file-locking-for-PID-file-crea.patch
Patch427:       0427-man-update-URL-refernce-in-daemon-7.patch
Patch428:       0428-conf-parser-never-consider-it-an-error-if-we-cannot-.patch
Patch429:       0429-socket-properly-handle-if-our-service-vanished-durin.patch
Patch430:       0430-keymap-Add-Lenovo-Enhanced-USB-Keyboard.patch
Patch431:       0431-keymap-Asus-EeePC-touchpad-toggle-key.patch
Patch432:       0432-udev-keyboard-also-hook-into-change-events.patch
Patch433:       0433-Do-not-unescape-unit-names-in-Install-section.patch
Patch434:       0434-util-ignore_file-should-not-allow-files-ending-with.patch
Patch435:       0435-udev-builtin-keyboard-do-tell-on-which-device-EVIOCS.patch
Patch436:       0436-tty-ask-password-agent-Do-tell-what-directory-we-fai.patch
Patch437:       0437-keyboard-add-Plantronics-.Audio-mute-button.patch
Patch438:       0438-hwdb-fix-case-sensitive-match.patch
Patch439:       0439-man-fix-references-to-sd_journal_cutoff_realtime_use.patch
Patch440:       0440-man-Searching-for-an-explanation-of-what-a-slice-uni.patch
Patch441:       0441-systemd-detect-virt-only-discover-Xen-domU.patch
Patch442:       0442-man-updates-to-the-passive-target-section.patch
Patch443:       0443-label-when-clearing-selinux-context-don-t-mangle-err.patch
Patch444:       0444-units-order-network-online.target-after-network.targ.patch
Patch445:       0445-core-fix-invalid-free-in-killall.patch
Patch446:       0446-install-fix-invalid-free-in-unit_file_mask.patch
Patch447:       0447-rpm-don-t-hardcode-the-binary-paths-in-the-macros-re.patch
Patch448:       0448-tmpfiles-set-up-selinux-label-proeprly-when-creating.patch
Patch449:       0449-util-add-files_same-helper-function.patch
Patch450:       0450-Add-strappenda3.patch
Patch451:       0451-unit-name-fix-detection-of-unit-templates-instances.patch
Patch452:       0452-conf-files-fix-when-for-root-logic.patch
Patch453:       0453-bootchart-set-white-background.patch
Patch454:       0454-backlight-always-prefer-firmware-platform-backlights.patch
Patch455:       0455-install-various-modernizations.patch
Patch456:       0456-install-simplify-and-clarify-disabling-logic-for-ins.patch
Patch457:       0457-install-when-looking-for-a-unit-file-for-enabling-se.patch
Patch458:       0458-install-make-sure-systemctl-disable-foobar-.service-.patch
Patch459:       0459-install-make-sure-that-root-mode-doesn-t-make-us-con.patch
Patch460:       0460-install-simplify-symlink-root-logic.patch
Patch461:       0461-backlight-include-ID_PATH-in-file-names-for-backligh.patch
Patch462:       0462-backlight-Fix-copy-paste-error-printing-an-unrelated.patch
Patch463:       0463-backlight-Avoid-restoring-brightness-to-an-unreadabl.patch
Patch464:       0464-backlight-do-nothing-if-max_brightness-is-0.patch
Patch465:       0465-backlight-unify-error-messages.patch
Patch466:       0466-backlight-handle-saved-brightness-exceeding-max-brig.patch
Patch467:       0467-backlight-Do-not-clamp-brightness-for-LEDs.patch
Patch468:       0468-cryptsetup-introduce-new-cryptsetup-pre.traget-unit-.patch
Patch469:       0469-rules-add-loop-control-and-btrfs-control-to-disk-gro.patch
Patch470:       0470-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch471:       0471-Fix-instance-argument-for-systemd-backlight-.service.patch
Patch472:       0472-socket-check-return-from-exec_spawn.patch
Patch473:       0473-getty-generator-properly-escape-instance-names.patch
Patch474:       0474-conf-files-include-root-in-returned-file-paths.patch
Patch475:       0475-shared-add-root-argument-to-search_and_fopen.patch
Patch476:       0476-shared-fix-search_and_fopen-with-alternate-roots.patch
Patch477:       0477-Reset-signal-mask-on-re-exec-to-init.patch
Patch478:       0478-core-clean-up-signal-reset-logic-when-reexec.patch
Patch479:       0479-util-treat-fuse.sshfs-as-a-network-filesystem.patch
Patch480:       0480-units-systemd-sysctl.service.in-run-after-load-modul.patch
Patch481:       0481-man-document-statically-loading-modules-for-sysctl-s.patch
Patch482:       0482-man-also-describe-an-udev-rule-for-bridge-sysctl.patch
Patch483:       0483-util-do-not-strip-dev-prefix-twice.patch
Patch484:       0484-core-transaction-avoid-misleading-error-message-when.patch
Patch485:       0485-core-snapshot-log-info-when-snapshots-are-created-an.patch
Patch486:       0486-vconsole-also-copy-character-maps-not-just-fonts-fro.patch
Patch487:       0487-core-You-can-not-put-the-cached-result-of-use_smack-.patch
Patch488:       0488-cryptsetup-don-t-add-unit-dependency-on-dev-null-dev.patch
Patch489:       0489-man-fix-path-in-crypttab-5.patch
Patch490:       0490-core-transaction-fix-cycle-break-attempts-outside-tr.patch
Patch491:       0491-journald-make-MaxFileSec-really-default-to-1month.patch
Patch492:       0492-rules-don-t-enable-usb-pm-for-Avocent-devices.patch
Patch493:       0493-units-remove-RefuseManualStart-from-units-which-are-.patch
Patch494:       0494-units-skip-mounting-tmp-if-it-is-a-symlink.patch
Patch495:       0495-man-sd_journal_next-fix-argument-in-example.patch
Patch496:       0496-man-sd_journal_get_data-fix-variable-naming-in-examp.patch
Patch497:       0497-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch498:       0498-hwdb-update.patch
Patch499:       0499-units-conditionalize-static-device-node-logic-on-CAP.patch
Patch500:       0500-units-conditionalize-configfs-and-debugfs-with-CAP_S.patch
Patch501:       0501-machine-don-t-return-uninitialized-variable.patch
Patch502:       0502-vconsole-setup-run-setfont-before-loadkeys.patch
Patch503:       0503-vconsole-setup-fix-inverted-error-messages.patch
Patch504:       0504-util-consider-0x7F-a-control-chracter-which-it-is-DE.patch
Patch505:       0505-service-flush-status-text-and-errno-values-each-time.patch
Patch506:       0506-accelerometer-Don-t-wait-for-new-data-from-the-senso.patch
Patch507:       0507-journal-compress-simplify-compress_blob.patch
Patch508:       0508-journal-compress-add-stream-compression-decompressio.patch
Patch509:       0509-journal-compress-improve-xz-compression-performance.patch
Patch510:       0510-hostnamed-add-a-new-chassis-type-for-watches.patch
Patch511:       0511-hostnamed-update-documentation-with-new-watch-chassi.patch
Patch512:       0512-units-make-ExecStopPost-action-part-of-ExecStart.patch
Patch513:       0513-shell-completion-man-beef-up-chassis-completions-and.patch
Patch514:       0514-rules-consistently-use-instead-of.patch
Patch515:       0515-rules-uaccess-add-ID_SOFTWARE_RADIO.patch
Patch516:       0516-journal-allow-files-with-no-data-whatsoever.patch
Patch517:       0517-units-serial-getty-.service-use-the-default-RestartS.patch
Patch518:       0518-build-sys-don-t-move-libgudev-to-lib.patch
Patch519:       0519-core-nicer-message-when-inotify-watches-are-exhauste.patch
Patch520:       0520-journal-reduce-test-journal-send-timeout-from-10s-to.patch
Patch521:       0521-socket-add-SocketUser-and-SocketGroup-for-chown-ing-.patch
Patch522:       0522-analyze-fix-crash-on-invalid-commandline.patch
Patch523:       0523-build-sys-fix-conftest.c-to-work-on-arm.patch
Patch524:       0524-nspawn-allow-EEXIST-on-mkdir_safe-home-uid.patch
Patch525:       0525-switch-root-umount-the-old-root-correctly.patch
Patch526:       0526-udev-builtin-keyboard-Allow-numeric-key-codes.patch
Patch527:       0527-keymap-Fix-HP-Pavillon-DV7.patch
Patch528:       0528-man-correct-references-to-DefaultTimeout-Sec.patch
Patch529:       0529-hwdb-update-format-description-and-document-reloadin.patch
Patch530:       0530-util-avoid-considering-dpkg-temporary-files-relevant.patch
Patch531:       0531-man-document-that-we-look-for-both-the-instance-s-an.patch
Patch532:       0532-bootchart-it-s-not-OK-to-return-1-from-a-main-progra.patch
Patch533:       0533-journald-Fix-off-by-one-error-in-Missed-X-kernel-mes.patch
Patch534:       0534-man-drop-references-to-removed-and-obsolete-systemct.patch
Patch535:       0535-sysctl-always-write-net.ipv4.conf.all.xyz-in-additio.patch
Patch536:       0536-kernel-install-90-loaderentry.install-fixed-cmdline-.patch
Patch537:       0537-units-fix-BindsTo-logic-when-applied-relative-to-ser.patch
Patch538:       0538-util-try-to-be-a-bit-more-NFS-compatible-when-checki.patch
Patch539:       0539-update-hwdb.patch
Patch540:       0540-systemctl-fail-in-the-case-that-no-unit-files-were-f.patch
Patch541:       0541-udev-hwdb-do-not-look-at-usb_device-parents.patch
Patch542:       0542-Document-.-.-udev-match-syntax.patch
Patch543:       0543-sd-journal-properly-convert-object-size-on-big-endia.patch
Patch544:       0544-sd-journal-verify-that-object-start-with-the-field-n.patch
Patch545:       0545-units-make-emergency.service-conflict-with-rescue.se.patch
Patch546:       0546-units-m4-is-not-needed-for-rescue.service.patch
Patch547:       0547-units-update-rescue.service-and-emergency.service.patch
Patch548:       0548-config-parser-fix-mem-leak.patch
Patch549:       0549-localed-log-locale-keymap-changes-in-detail.patch
Patch550:       0550-localed-introduce-helper-function-to-simplify-matchi.patch
Patch551:       0551-localed-check-for-partially-matching-converted-keyma.patch
Patch552:       0552-exit-status-fix-URL-in-comment.patch
Patch553:       0553-man-fix-references-to-systemctl-man-page-which-is-no.patch
Patch554:       0554-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch555:       0555-hwdb-update.patch
Patch556:       0556-journal-do-not-leak-mmaps-on-OOM.patch
Patch557:       0557-manager-use-correct-cleanup-function.patch
Patch558:       0558-analyze-avoid-a-null-dereference.patch
Patch559:       0559-core-smack-setup-Actually-allow-for-succesfully-load.patch
Patch560:       0560-core-fix-a-potential-mem-leak.patch
Patch561:       0561-core-use-correct-function-to-free-CalendarSpec.patch
Patch562:       0562-udev-rules-close-empty-file.patch
Patch563:       0563-man-use-the-escape-for-in-example-instead-of-space.patch
Patch564:       0564-logind-add-support-for-Triton2-Power-Button.patch
Patch565:       0565-systemd-tmpfiles-Fix-IGNORE_DIRECTORY_PATH-age-handl.patch
Patch566:       0566-shell-completion-zsh-journalctl-s-b-changes.patch
Patch567:       0567-logind-add-support-for-TPS65217-Power-Button.patch
Patch568:       0568-journalctl-do-not-output-reboot-markers-when-running.patch
Patch569:       0569-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch570:       0570-bootchart-use-n-a-if-PRETTY_NAME-is-not-found.patch
Patch571:       0571-fileio-label-return-error-when-writing-fails.patch
Patch572:       0572-core-don-t-allow-enabling-if-unit-is-masked.patch
Patch573:       0573-core-map-the-rescue-argument-to-rescue.target.patch
Patch574:       0574-man-systemctl-document-enable-on-masked-units.patch
Patch575:       0575-man-document-the-new-rescue-kernel-command-line-opti.patch
Patch576:       0576-sd-journal-do-not-reset-sd_j_enumerate_unique-positi.patch
Patch577:       0577-sd-journal-change-check-to-assert.patch
Patch578:       0578-sd-journal-fix-sd_journal_enumerate_unique-skipping-.patch
Patch579:       0579-journalctl-use-pager-for-list-boots.patch
Patch580:       0580-python-systemd-avoid-hitting-assert-in-__exit__.patch
Patch581:       0581-shell-completion-restore-completion-for-p.patch
Patch582:       0582-zsh-completion-Move-output-modes-to-autoload.patch
Patch583:       0583-shell-completion-systemd-analyze-verify-systemctl-li.patch
Patch584:       0584-shell-completion-prevent-mangling-unit-names.patch
Patch585:       0585-bash-completion-use-list-unit-files-to-get-all-units.patch
Patch586:       0586-shell-completion-prevent-mangling-unit-names-bash.patch
Patch587:       0587-completion-filter-templates-from-restartable-units.patch
Patch588:       0588-shell-completion-fix-completion-of-inactive-units.patch
Patch589:       0589-shell-completion-propose-templates-for-disable-re-en.patch
Patch590:       0590-man-we-don-t-have-Wanted-dependency.patch
Patch591:       0591-man-fix-localectl-set-x11-keymap-syntax-description.patch
Patch592:       0592-journalctl-correct-help-text-for-until.patch
Patch593:       0593-calendarspec-fix-typo-in-annually.patch
Patch594:       0594-systemctl-do-not-ignore-errors-in-symlink-removal.patch
Patch595:       0595-journalctl-man-allow-only-between-terms.patch
Patch596:       0596-core-some-more-_cleanup_free_.patch
Patch597:       0597-core-do-not-add-dependencies-to-self.patch
Patch598:       0598-udev-timeout-increase-timeout.patch
Patch599:       0599-Update-hwdb-60-keyboard.hwdb-to-version-from-master.patch
Patch600:       0600-units-tmpfiles-setup-dev-allow-unsafe-file-creation-.patch
Patch601:       0601-shell-completion-systemctl-set-default-get-default-i.patch
Patch602:       0602-bash-completion-rework-startable-restartable-units-o.patch
Patch603:       0603-systemctl-let-list-units-unit-files-honour-type.patch
Patch604:       0604-systemctl-obey-state-in-list-unit-files.patch
Patch605:       0605-bash-completion-use-improved-filtering-to-make-thing.patch
Patch606:       0606-zsh-completion-update-start-restart-completions.patch
Patch607:       0607-udev-bump-event-timeout-in-two-more-places.patch
Patch608:       0608-journald-always-add-syslog-facility-for-messages-com.patch
Patch609:       0609-machinectl-correctly-supply-user-when-connecting-ove.patch
Patch610:       0610-nspawn-fix-invocation-of-the-raw-clone-system-call-o.patch
Patch611:       0611-hwdb-ignore-brightness-keys-on-Dell-Inspiron.patch
Patch612:       0612-kernel-install-90-loaderentry.install-fix-cmdline-pa.patch
Patch613:       0613-manager-print-fatal-errors-on-the-console-too.patch
Patch614:       0614-journald-when-we-detect-the-journal-file-we-are-abou.patch
Patch615:       0615-hwdb-add-a-touchpad-hwdb.patch

# kernel-install patch for grubby, drop if grubby is obsolete
Patch1000:      kernel-install-grubby.patch


# Pantheon backport of cgroup cache controller optimizations from systemd master branch (2013-11-21) -joe
Patch2000:      2000-cgroups-Cache-controller-masks-and-optimize-queues.patch
Patch2001:      2001-install-Assume-.wants-symlinks-have-the-same-name-as.patch

%global num_patches %{lua: c=0; for i,p in ipairs(patches) do c=c+1; end; print(c);}

BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  dbus-devel
BuildRequires:  libacl-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libblkid-devel
BuildRequires:  xz-devel
BuildRequires:  kmod-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  qrencode-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gperf
BuildRequires:  gawk
BuildRequires:  gtk-doc
BuildRequires:  python2-devel
BuildRequires:  python3-devel
%if %{defined gitcommit}%{num_patches}
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
%if %{num_patches}
BuildRequires:  git
%endif
Requires(post): coreutils
Requires(post): sed
Requires(post): acl
Requires(pre):  coreutils
Requires(pre):  /usr/bin/getent
Requires(pre):  /usr/sbin/groupadd
Requires:       dbus
Requires:       %{name}-libs = %{version}-%{release}
Requires:       kmod >= 15-2
Requires:       diffutils
Provides:       /bin/systemctl
Provides:       /sbin/shutdown
Provides:       syslog
Provides:       systemd-units = %{version}-%{release}
Provides:       udev = %{version}
Obsoletes:      udev < 183
Obsoletes:      system-setup-keyboard < 0.9
Provides:       system-setup-keyboard = 0.9
Obsoletes:      nss-myhostname < 0.4
Provides:       nss-myhostname = 0.4
# For the journal-gateway split in F20, drop at F22
Obsoletes:      systemd < 204-10
# systemd-analyze got merged in F19, drop at F21
Obsoletes:      systemd-analyze < 198
Provides:       systemd-analyze = 198
# systemd-sysv-convert was removed in f20: https://fedorahosted.org/fpc/ticket/308
Obsoletes:      systemd-sysv < 206
Provides:       systemd-sysv = 206
# https://bugzilla.redhat.com/show_bug.cgi?id=1026860
Conflicts:      lvm2 < 2.02.103-4

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package libs
Summary:        systemd libraries
License:        LGPLv2+ and MIT
Obsoletes:      libudev < 183
Obsoletes:      systemd < 185-4
Conflicts:      systemd < 185-4

%description libs
Libraries for systemd and udev, as well as the systemd PAM module.

%package devel
Summary:        Development headers for systemd
License:        LGPLv2+ and MIT
Requires:       %{name} = %{version}-%{release}
Provides:       libudev-devel = %{version}
Obsoletes:      libudev-devel < 183

%description devel
Development headers and auxiliary files for developing applications for systemd.

%package python
Summary:        Python 2 bindings for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%package python3
Summary:        Python 3 bindings for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description python
This package contains bindings which allow Python 2 programs to use
systemd APIs

%description python3
This package contains bindings which allow Python 3 programs to use
systemd APIs

%package -n libgudev1
Summary:        Libraries for adding libudev support to applications that use glib
Conflicts:      filesystem < 3
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}

%description -n libgudev1
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n libgudev1-devel
Summary:        Header files for adding libudev support to applications that use glib
Requires:       libgudev1 = %{version}-%{release}
License:        LGPLv2+

%description -n libgudev1-devel
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%package journal-gateway
Summary:        Gateway for serving journal events over the network using HTTP
Requires:       %{name} = %{version}-%{release}
License:        LGPLv2+
Requires(pre):    /usr/bin/getent
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# For the journal-gateway split in F20, drop at F22
Obsoletes:      systemd < 204-10

%description journal-gateway
systemd-journal-gatewayd serves journal events over the network using HTTP.

%prep
%setup -q %{?gitcommit:-n %{name}-git%{gitcommit}}

%if %{num_patches}
    git init
    git config user.email "systemd-maint@redhat.com"
    git config user.name "Fedora systemd team"
    git add .
    git commit -a -q -m "%{version} baseline."

    # Apply all the patches.
    git am \
        --exclude .gitignore \
        --exclude docs/.gitignore \
        --exclude docs/gudev/.gitignore \
        --exclude docs/libudev/.gitignore \
        --exclude docs/sysvinit/.gitignore \
        --exclude docs/var-log/.gitignore \
        --exclude hwdb/.gitignore \
        --exclude m4/.gitignore \
        --exclude man/.gitignore \
        --exclude po/.gitignore \
        --exclude rules/.gitignore \
        --exclude src/.gitignore \
        --exclude src/analyze/.gitignore \
        --exclude src/core/.gitignore \
        --exclude src/gudev/.gitignore \
        --exclude src/hostname/.gitignore \
        --exclude src/journal/.gitignore \
        --exclude src/libsystemd-daemon/.gitignore \
        --exclude src/libsystemd-id128/.gitignore \
        --exclude src/libudev/.gitignore \
        --exclude src/locale/.gitignore \
        --exclude src/login/.gitignore \
        --exclude src/python-systemd/.gitignore \
        --exclude src/python-systemd/docs/.gitignore \
        --exclude src/timedate/.gitignore \
        --exclude src/udev/.gitignore \
        --exclude src/udev/scsi_id/.gitignore \
        --exclude sysctl.d/.gitignore \
        --exclude test/.gitignore \
        --exclude units/.gitignore \
        --exclude units/user/.gitignore \
        --exclude hwdb/ids-update.pl \
        %{patches}
%endif

%build
%if %{defined gitcommit}
    ./autogen.sh
%else
    %if %{num_patches}
        autoreconf
    %endif
%endif

# first make python3 while source directory is empty
rm -rf build2 build3
mkdir build2
mkdir build3

pushd build3
%define _configure ../configure
%configure \
        --libexecdir=%{_prefix}/lib \
        --disable-manpages \
        --with-sysvinit-path=/etc/rc.d/init.d \
        --with-rc-local-script-path-start=/etc/rc.d/rc.local \
        PYTHON=%{__python3}
make %{?_smp_mflags} GCC_COLORS="" V=1
popd

pushd build2
%configure \
        --libexecdir=%{_prefix}/lib \
        --enable-gtk-doc \
        --with-sysvinit-path=/etc/rc.d/init.d \
        --with-rc-local-script-path-start=/etc/rc.d/rc.local
make %{?_smp_mflags} V=1
popd

%install
# first install python3 so the binaries are overwritten by the python2 ones
pushd build3
%make_install
popd
pushd build2
%make_install
popd

find %{buildroot} \( -name '*.a' -o -name '*.la' \) -delete

# udev links
mkdir -p %{buildroot}/%{_sbindir}
ln -sf ../bin/udevadm %{buildroot}%{_sbindir}/udevadm

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
ln -s ../lib/systemd/systemd %{buildroot}%{_sbindir}/init
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/reboot
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/halt
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/poweroff
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/shutdown
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/telinit
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the user deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants

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

# Temporary workaround for #1002806
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/poweroff.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/rescue.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/multi-user.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/graphical.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/reboot.target.wants
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/poweroff.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/rescue.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/multi-user.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/graphical.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/reboot.target.wants/

# Make sure the user generators dir exists too
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-generators
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-generators

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/localtime
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Install Fedora default preset policy
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-preset/
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Make sure the shutdown/sleep drop-in dirs exist
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-shutdown/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep/

# Make sure the NTP units dir exists
mkdir -p %{buildroot}%{_prefix}/lib/systemd/ntp-units.d/

# Make sure directories in /var exist
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
mkdir -p %{buildroot}%{_localstatedir}/log/journal
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin

# Install rsyslog fragment
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/rsyslog.d/

# Install yum protection fragment
mkdir -p %{buildroot}%{_sysconfdir}/yum/protected.d/
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/yum/protected.d/systemd.conf

# Don't package the kernel.core_pattern, we need minidumps working before
# this can replace Fedora's current core dump handling.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/50-coredump.conf

%pre
getent group cdrom >/dev/null 2>&1 || groupadd -r -g 11 cdrom >/dev/null 2>&1 || :
getent group tape >/dev/null 2>&1 || groupadd -r -g 33 tape >/dev/null 2>&1 || :
getent group dialout >/dev/null 2>&1 || groupadd -r -g 18 dialout >/dev/null 2>&1 || :
getent group floppy >/dev/null 2>&1 || groupadd -r -g 19 floppy >/dev/null 2>&1 || :
getent group systemd-journal >/dev/null 2>&1 || groupadd -r -g 190 systemd-journal 2>&1 || :

systemctl stop systemd-udevd-control.socket systemd-udevd-kernel.socket systemd-udevd.service >/dev/null 2>&1 || :

%post
systemd-machine-id-setup >/dev/null 2>&1 || :
/usr/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :
systemctl daemon-reexec >/dev/null 2>&1 || :
systemctl start systemd-udevd.service >/dev/null 2>&1 || :
udevadm hwdb --update >/dev/null 2>&1 || :
journalctl --update-catalog >/dev/null 2>&1 || :
systemd-tmpfiles --create >/dev/null 2>&1 || :

# Make sure new journal files will be owned by the "systemd-journal" group
chgrp systemd-journal /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :
chmod g+s /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :

# Move old stuff around in /var/lib
mv %{_localstatedir}/lib/random-seed %{_localstatedir}/lib/systemd/random-seed >/dev/null 2>&1 || :
mv %{_localstatedir}/lib/backlight %{_localstatedir}/lib/systemd/backlight >/dev/null 2>&1 || :

# Stop-gap until rsyslog.rpm does this on its own. (This is supposed
# to fail when the link already exists)
ln -s /usr/lib/systemd/system/rsyslog.service /etc/systemd/system/syslog.service >/dev/null 2>&1 || :

# Services we install by default, and which are controlled by presets.
if [ $1 -eq 1 ] ; then
        systemctl preset \
                getty@tty1.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :
fi

# sed-fu to add myhostname to the hosts line of /etc/nsswitch.conf
if [ -f /etc/nsswitch.conf ] ; then
        sed -i.bak -e '
                /^hosts:/ !b
                /\<myhostname\>/ b
                s/[[:blank:]]*$/ myhostname/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi

# Apply ACL to the journal directory
setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx /var/log/journal/ >/dev/null 2>&1 || :

%postun
if [ $1 -ge 1 ] ; then
        systemctl daemon-reload > /dev/null 2>&1 || :
        systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :

        rm -f /etc/systemd/system/default.target >/dev/null 2>&1 || :

        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.bak -e '
                        /^hosts:/ !b
                        s/[[:blank:]]\+myhostname\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%pre journal-gateway
getent group systemd-journal-gateway >/dev/null 2>&1 || groupadd -r -g 191 systemd-journal-gateway 2>&1 || :
getent passwd systemd-journal-gateway >/dev/null 2>&1 || useradd -r -l -u 191 -g systemd-journal-gateway -d %{_localstatedir}/log/journal -s /sbin/nologin -c "Journal Gateway" systemd-journal-gateway >/dev/null 2>&1 || :

%post journal-gateway
%systemd_post systemd-journal-gatewayd.socket systemd-journal-gatewayd.service

%preun journal-gateway
%systemd_preun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service

%postun journal-gateway
%systemd_postun_with_restart systemd-journal-gatewayd.service

%files
%doc %{_docdir}/systemd
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/system-generators
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/system-preset
%dir %{_prefix}/lib/systemd/user-preset
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/systemd/system-sleep
%dir %{_prefix}/lib/systemd/catalog
%dir %{_prefix}/lib/systemd/ntp-units.d
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%dir %{_prefix}/lib/kernel
%dir %{_prefix}/lib/kernel/install.d
%dir %{_datadir}/systemd
%dir %{_datadir}/pkgconfig
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_localstatedir}/log/journal
%dir %{_localstatedir}/lib/systemd
%dir %{_localstatedir}/lib/systemd/catalog
%dir %{_localstatedir}/lib/systemd/coredump
%ghost %dir %{_localstatedir}/lib/systemd/backlight
%ghost %{_localstatedir}/lib/systemd/random-seed
%ghost %{_localstatedir}/lib/systemd/catalog/database

%{_localstatedir}/log/README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.machine1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%config(noreplace) %{_sysconfdir}/rsyslog.d/listen.conf
%config(noreplace) %{_sysconfdir}/yum/protected.d/systemd.conf
%config(noreplace) %{_sysconfdir}/pam.d/systemd-user
%ghost %{_sysconfdir}/udev/hwdb.bin
%{_rpmconfigdir}/macros.d/macros.systemd
%{_sysconfdir}/xdg/systemd
%{_sysconfdir}/rc.d/init.d/README
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/localtime
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%dir %{_sysconfdir}/X11/xorg.conf.d
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
%{_bindir}/systemctl
%{_bindir}/systemd-notify
%{_bindir}/systemd-analyze
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-machine-id-setup
%{_bindir}/loginctl
%{_bindir}/journalctl
%{_bindir}/machinectl
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-run
%caps(cap_dac_override,cap_sys_ptrace=pe) %{_bindir}/systemd-detect-virt
%{_bindir}/systemd-inhibit
%{_bindir}/hostnamectl
%{_bindir}/localectl
%{_bindir}/timedatectl
%{_bindir}/bootctl
%{_bindir}/systemd-coredumpctl
%{_bindir}/udevadm
%{_bindir}/kernel-install
%{_prefix}/lib/systemd/systemd
%exclude %{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%exclude %{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_prefix}/lib/systemd/systemd-*
%{_prefix}/lib/udev
%{_prefix}/lib/systemd/system-generators/systemd-cryptsetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-getty-generator
%{_prefix}/lib/systemd/system-generators/systemd-rc-local-generator
%{_prefix}/lib/systemd/system-generators/systemd-fstab-generator
%{_prefix}/lib/systemd/system-generators/systemd-system-update-generator
%{_prefix}/lib/systemd/system-generators/systemd-efi-boot-generator
%{_prefix}/lib/systemd/system-generators/systemd-gpt-auto-generator
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/sysctl.d/50-default.conf
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%{_prefix}/lib/systemd/catalog/systemd.catalog
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_sbindir}/init
%{_sbindir}/reboot
%{_sbindir}/halt
%{_sbindir}/poweroff
%{_sbindir}/shutdown
%{_sbindir}/telinit
%{_sbindir}/runlevel
%{_sbindir}/udevadm
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%exclude %{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/*
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/pkgconfig/systemd.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files libs
%{_libdir}/security/pam_systemd.so
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libsystemd-daemon.so.*
%{_libdir}/libsystemd-login.so.*
%{_libdir}/libsystemd-journal.so.*
%{_libdir}/libsystemd-id128.so.*
%{_libdir}/libudev.so.*

%files devel
%dir %{_includedir}/systemd
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_libdir}/libsystemd-journal.so
%{_libdir}/libsystemd-id128.so
%{_libdir}/libudev.so
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/sd-shutdown.h
%{_includedir}/libudev.h
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc
%{_libdir}/pkgconfig/libsystemd-journal.pc
%{_libdir}/pkgconfig/libsystemd-id128.pc
%{_libdir}/pkgconfig/libudev.pc
%{_mandir}/man3/*
%dir %{_datadir}/gtk-doc/html/libudev
%{_datadir}/gtk-doc/html/libudev/*

%files python
%{python_sitearch}/systemd

%files python3
%{python3_sitearch}/systemd

%files -n libgudev1
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files -n libgudev1-devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*

%files journal-gateway
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_datadir}/systemd/gatewayd

%changelog
* Thu Feb  5 2015 Jan Synáček <jsynacek@redhat.com> - 208-30
- RFE: journal: automatically rotate the file if it is unlinked (#1171719)
- Add a touchpad hwdb (#1189319)

* Tue Jan  6 2015 Jan Synáček <jsynacek@redhat.com> - 208-29
- Two backlight events upon single keypress on Dell Inspiron 1520 (#1141525)
- kernel-install/90-loaderentry.install broken cmdline parsing: never installs kernels (#1166531)
- systemd does not properly report errors when booting fails because it cannot load selinux policy (#1155468)

* Mon Jan  5 2015 Jan Synáček <jsynacek@redhat.com> - 208-29
- systemd-nspawn doesn't work on s390/s390x (#1175394)

* Mon Nov 10 2014 Jan Synáček <jsynacek@redhat.com> - 208-28
- Always add syslog facility for messages coming from kmsg (#1161995)
- Correctly apply user when connecting over ssh (#1156363)

* Thu Nov 06 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-27
- Bump kmod requirement to make sure they are updated in lockstep
- Increase the udev timeout to 180 seconds in two more places (#1091513)

* Wed Oct 29 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-26
- Better fixes for completion (#790768)
- Do not change device permissions with tmpfiles after boot (#1147248)

* Sun Oct 26 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-25
- Various journal reading fixes (#1052262, #1110712, possibly #1073830, #1095962, and #1139694)
- Increase udev worker timeout to 180 seconds (#1109478, possibly #1091513)
- Shell completion for inactive units is improved (#790768)
- Other small fixes (#1128360, #1149069, #1124843, #1049306)
- Change libgudev1 to only require systemd-libs (#727499), there's
  no need to require full systemd stack.

* Wed Oct 01 2014 Kay Sievers <kay@redhat.com> - 208-24
- revert "don't reset selinux context during CHANGE events"

* Wed Oct 01 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-23
- add temporary workaround for #1147910
- don't reset selinux context during CHANGE events

* Mon Sep 22 2014 Jan Synacek <jsynacek@redhat.com> - 208-22
- Fix systemd-nspawn with -u (#1145108)

* Thu Jul 24 2014 Michal Schmidt <mschmidt@redhat.com> - 208-21
- Create temporary files after installation (#1084052, fix from #1101983)

* Sat Jul 19 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-20
- Make it easier to apply sysctl settings delaying
  systemd-sysctl.service after modules have been loaded
- Terminal font loading fixes
- Man page updates (#1022977)
- Hardware database update
- Journal XZ compression settings updated for speed
- Add "watch" as new chassis type
- Add udev tag "ID_SOFTWARE_RADIO" to allow access for users
- SocketUser and SocketGroup settings backported from v214 (#1119282)
- Other small tweaks (#996133)

* Fri Jun 20 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-19
- Fix patch
- Some more --root support and other assorted fixes

* Tue Jun 17 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-18
- Fix permissions on new journal files (#1047729)
- Fix systemd-delta output (#1088418)
- Fix some (potential) bad memory accesses
- Fix cryptsetup keysize handling
- Fix handling of jobs during systemd reload
- Fix detection of container virtualization under KVM and Xen domU
- Update hardware database
- Some small documentation updates (#1096067, #1073402, #1088057)
- Make SYSV $network be equivalent to network-online, not network target
- Do not skip RUN execution when udev fails to rename network device
- Minor overhaul of systmemctl install handling with symlinked units
  and --root
- Make systemd close sockets asynchronously to prevent stalls
- Allow local users to hibernate
- Fix selinux policy reload on switch-root
- Restore backlight also for "raw" devices (#1108019)
- Make backlight paths stable (backlight settings will probably by lost on
  update), and sanitize restored values (#1062638)
- Add cryptsetup-pre.target (#1097938)
- Make btrfs-control and loop-control owned by group 'disk' (#1045432)

* Wed Jun 11 2014 Michal Sekletar <msekleta@redhat.com> - 208-17
- Log debug message when Abandon() fails (#1105857)
- Reduce amount of messages logged to kmsg when debug in enabled
- Hardware database updates
- Misc fixes (systemd-delta, journald, bash completion, docs)

* Mon Apr 07 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-16
- Rework systemd-logind shutdown logic (#1032695)
- Fix saving of logind session state and change notifications
- Enable timeouts for generator execution
- Recognize buttonless joystick types
  (https://bugs.freedesktop.org/show_bug.cgi?id=70734)
- Fix policykit check for reboot
- Fix udev behaviour for unconnected loop devices
- Fix overflow on password entry (#1084286)
- Update hardware database
- Consider glusterfs and fuse.glusterfs to be networked filesystems
- Fix journalctl -o export for multiline messages
- Fix get_catalog() in systemd-python for UUID arguments under Python 3
- Documentation updates
- Fix for #626477.

* Sun Feb 23 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-15
- Backport some small patches, mostly completion updates and
  documentation fixes (#1069393, #1047568, #1047039, #1070970, #1061031)
- Make sclp_line, ttysclp and 3270/tty owned by group tty
- Allow key-slot= in crypttab
- Update database of bluetooth identifiers

* Sun Feb 23 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-15
- Enable dnssec-triggerd.service by default (#1060754)

* Mon Feb 17 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-14
- Back out patch which causes user manager to be destroyed when unneeded
  and spams logs (#1053315)

* Sun Feb 16 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-13
- A different fix for #1023820 taken from Mageia
- Backported fix for #997031
- Hardward database updates, man pages improvements, a few small memory
  leaks, utf-8 correctness and completion fixes
- Support for key-slot option in crypttab

* Sat Jan 25 2014 Ville Skyttä <ville.skytta@iki.fi> - 208-12
- Own the %%{_prefix}/lib/kernel(/*) and %%{_datadir}/zsh(/*) dirs.

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-11
- Backport a few fixes, relevant documentation updates, and HWDB changes
  (#1051797, #1051768, #1047335, #1047304, #1047186, #1045849, #1043304,
   #1043212, #1039351, #1031325, #1023820, #1017509, #953077)

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-10
- Remove patch for #1026860 now that LVM rules have been updated

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-9
- Apply two patches for #1026860

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-8
- Back out patches for bugs which are not freeze-excepted (only #1006386?
  remains)

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-7
- Backport patches (#1023041, #1036845, #1006386?)
- HWDB update
- Some small new features: nspawn --drop-capability=, running PID 1 under
  valgrind, "yearly" and "annually" in calendar specifications
- Some small documentation and logging updates

* Tue Nov 19 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-6
- Back kmod dependency version bump out

* Tue Nov 19 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-5
- Use unit name in PrivateTmp= directories (#957439)
- Update manual pages, completion scripts, and hardware database
- Configurable Timeouts/Restarts default values
- Support printing of timestamps on the console
- Fix some corner cases in detecting when writing to the console is safe
- Python API: convert keyword values to string, fix sd_is_booted() wrapper
- Do not tread missing /sbin/fsck.btrfs as an error (#1015467)
- Allow masking of fsck units
- Advertise hibernation to swap files
- Fix SO_REUSEPORT settings
- Prefer converted xkb keymaps to legacy keymaps (#981805, #1026872)
- Make use of newer kmod
- Assorted bugfixes: #1017161, #967521, #988883, #1027478, #821723, #1014303

* Tue Oct 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-4
- Add temporary fix for #1002806

* Mon Oct 21 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-3
- Backport a bunch of fixes and hwdb updates

* Wed Oct 2 2013 Lennart Poettering <lpoetter@redhat.com> - 208-2
- Move old random seed and backlight files into the right place

* Wed Oct 2 2013 Lennart Poettering <lpoetter@redhat.com> - 208-1
- New upstream release

* Thu Sep 26 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 207-5
- Do not create /var/var/... dirs

* Wed Sep 18 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 207-4
- Fix policykit authentication
- Resolves: rhbz#1006680

* Tue Sep 17 2013 Harald Hoyer <harald@redhat.com> 207-3
- fixed login
- Resolves: rhbz#1005233

* Mon Sep 16 2013 Harald Hoyer <harald@redhat.com> 207-2
- add some upstream fixes for 207
- fixed swap activation
- Resolves: rhbz#1008604

* Fri Sep 13 2013 Lennart Poettering <lpoetter@redhat.com> - 207-1
- New upstream release

* Fri Sep 06 2013 Harald Hoyer <harald@redhat.com> 206-11
- support "debug" kernel command line parameter
- journald: fix fd leak in journal_file_empty
- journald: fix vacuuming of archived journals
- libudev: enumerate - do not try to match against an empty subsystem
- cgtop: fixup the online help
- libudev: fix memleak when enumerating childs

* Wed Sep 04 2013 Harald Hoyer <harald@redhat.com> 206-10
- Do not require grubby, lorax now takes care of grubby
- cherry-picked a lot of patches from upstream

* Tue Aug 27 2013 Dennis Gilmore <dennis@ausil.us> - 206-9
- Require grubby, Fedora installs require grubby,
- kernel-install took over from new-kernel-pkg
- without the Requires we are unable to compose Fedora
- everyone else says that since kernel-install took over
- it is responsible for ensuring that grubby is in place
- this is really what we want for Fedora

* Tue Aug 27 2013 Kay Sievers <kay@redhat.com> - 206-8
- Revert "Require grubby its needed by kernel-install"

* Mon Aug 26 2013 Dennis Gilmore <dennis@ausil.us> 206-7
- Require grubby its needed by kernel-install

* Thu Aug 22 2013 Harald Hoyer <harald@redhat.com> 206-6
- kernel-install now understands kernel flavors like PAE

* Tue Aug 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 206-5
- add sddm.service to preset file (#998978)

* Fri Aug 16 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 206-4
- Filter out provides for private python modules.
- Add requires on kmod >= 14 (#990994).

* Sun Aug 11 2013 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 206-3
- New systemd-python3 package (#976427).
- Add ownership of a few directories that we create (#894202).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Kay Sievers <kay@redhat.com> - 206-1
- New upstream release
  Resolves (#984152)

* Wed Jul  3 2013 Lennart Poettering <lpoetter@redhat.com> - 205-1
- New upstream release

* Wed Jun 26 2013 Michal Schmidt <mschmidt@redhat.com> 204-10
- Split systemd-journal-gateway subpackage (#908081).

* Mon Jun 24 2013 Michal Schmidt <mschmidt@redhat.com> 204-9
- Rename nm_dispatcher to NetworkManager-dispatcher in default preset (#977433)

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-8
- fix, which helps to sucessfully browse journals with
  duplicated seqnums

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-7
- fix duplicate message ID bug
Resolves: rhbz#974132

* Thu Jun 06 2013 Harald Hoyer <harald@redhat.com> 204-6
- introduce 99-default-disable.preset

* Thu Jun  6 2013 Lennart Poettering <lpoetter@redhat.com> - 204-5
- Rename 90-display-manager.preset to 85-display-manager.preset so that it actually takes precedence over 90-default.preset's "disable *" line (#903690)

* Tue May 28 2013 Harald Hoyer <harald@redhat.com> 204-4
- Fix kernel-install (#965897)

* Wed May 22 2013 Kay Sievers <kay@redhat.com> - 204-3
- Fix kernel-install (#965897)

* Thu May  9 2013 Lennart Poettering <lpoetter@redhat.com> - 204-2
- New upstream release
- disable isdn by default (#959793)

* Tue May 07 2013 Harald Hoyer <harald@redhat.com> 203-2
- forward port kernel-install-grubby.patch

* Tue May  7 2013 Lennart Poettering <lpoetter@redhat.com> - 203-1
- New upstream release

* Wed Apr 24 2013 Harald Hoyer <harald@redhat.com> 202-3
- fix ENOENT for getaddrinfo
- Resolves: rhbz#954012 rhbz#956035
- crypt-setup-generator: correctly check return of strdup
- logind-dbus: initialize result variable
- prevent library underlinking

* Fri Apr 19 2013 Harald Hoyer <harald@redhat.com> 202-2
- nspawn create empty /etc/resolv.conf if necessary
- python wrapper: add sd_journal_add_conjunction()
- fix s390 booting
- Resolves: rhbz#953217

* Thu Apr 18 2013 Lennart Poettering <lpoetter@redhat.com> - 202-1
- New upstream release

* Tue Apr 09 2013 Michal Schmidt <mschmidt@redhat.com> - 201-2
- Automatically discover whether to run autoreconf and add autotools and git
  BuildRequires based on the presence of patches to be applied.
- Use find -delete.

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 201-1
- New upstream release

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 200-4
- Update preset file

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-3
- Remove NetworkManager-wait-online.service from presets file again, it should default to off

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-2
- New upstream release

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-2
- Add NetworkManager-wait-online.service to the presets file

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-1
- New upstream release

* Mon Mar 18 2013 Michal Schmidt <mschmidt@redhat.com> 198-7
- Drop /usr/s?bin/ prefixes.

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-6
- run autogen to pickup all changes

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-5
- do not mount anything, when not running as pid 1
- add initrd.target for systemd in the initrd

* Wed Mar 13 2013 Harald Hoyer <harald@redhat.com> 198-4
- fix switch-root and local-fs.target problem
- patch kernel-install to use grubby, if available

* Fri Mar 08 2013 Harald Hoyer <harald@redhat.com> 198-3
- add Conflict with dracut < 026 because of the new switch-root isolate

* Thu Mar  7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-2
- Create required users

* Thu Mar 7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-1
- New release
- Enable journal persistancy by default

* Sun Feb 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 197-3
- Bump for ARM

* Fri Jan 18 2013 Michal Schmidt <mschmidt@redhat.com> - 197-2
- Added qemu-guest-agent.service to presets (Lennart, #885406).
- Add missing pygobject3-base to systemd-analyze deps (Lennart).
- Do not require hwdata, it is all in the hwdb now (Kay).
- Drop dependency on dbus-python.

* Tue Jan  8 2013 Lennart Poettering <lpoetter@redhat.com> - 197-1
- New upstream release

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-4
- Enable rngd.service by default (#857765).

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-3
- Disable hardening on s390(x) because PIE is broken there and produces
  text relocations with __thread (#868839).

* Wed Dec 05 2012 Michal Schmidt <mschmidt@redhat.com> - 196-2
- added spice-vdagentd.service to presets (Lennart, #876237)
- BR cryptsetup-devel instead of the legacy cryptsetup-luks-devel provide name
  (requested by Milan Brož).
- verbose make to see the actual build flags

* Wed Nov 21 2012 Lennart Poettering <lpoetter@redhat.com> - 196-1
- New upstream release

* Tue Nov 20 2012 Lennart Poettering <lpoetter@redhat.com> - 195-8
- https://bugzilla.redhat.com/show_bug.cgi?id=873459
- https://bugzilla.redhat.com/show_bug.cgi?id=878093

* Thu Nov 15 2012 Michal Schmidt <mschmidt@redhat.com> - 195-7
- Revert udev killing cgroup patch for F18 Beta.
- https://bugzilla.redhat.com/show_bug.cgi?id=873576

* Fri Nov 09 2012 Michal Schmidt <mschmidt@redhat.com> - 195-6
- Fix cyclical dep between systemd and systemd-libs.
- Avoid broken build of test-journal-syslog.
- https://bugzilla.redhat.com/show_bug.cgi?id=873387
- https://bugzilla.redhat.com/show_bug.cgi?id=872638

* Thu Oct 25 2012 Kay Sievers <kay@redhat.com> - 195-5
- require 'sed', limit HOSTNAME= match

* Wed Oct 24 2012 Michal Schmidt <mschmidt@redhat.com> - 195-4
- add dmraid-activation.service to the default preset
- add yum protected.d fragment
- https://bugzilla.redhat.com/show_bug.cgi?id=869619
- https://bugzilla.redhat.com/show_bug.cgi?id=869717

* Wed Oct 24 2012 Kay Sievers <kay@redhat.com> - 195-3
- Migrate /etc/sysconfig/ i18n, keyboard, network files/variables to
  systemd native files

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-2
- Provide syslog because the journal is fine as a syslog implementation

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=831665
- https://bugzilla.redhat.com/show_bug.cgi?id=847720
- https://bugzilla.redhat.com/show_bug.cgi?id=858693
- https://bugzilla.redhat.com/show_bug.cgi?id=863481
- https://bugzilla.redhat.com/show_bug.cgi?id=864629
- https://bugzilla.redhat.com/show_bug.cgi?id=864672
- https://bugzilla.redhat.com/show_bug.cgi?id=864674
- https://bugzilla.redhat.com/show_bug.cgi?id=865128
- https://bugzilla.redhat.com/show_bug.cgi?id=866346
- https://bugzilla.redhat.com/show_bug.cgi?id=867407
- https://bugzilla.redhat.com/show_bug.cgi?id=868603

* Wed Oct 10 2012 Michal Schmidt <mschmidt@redhat.com> - 194-2
- Add scriptlets for migration away from systemd-timedated-ntp.target

* Wed Oct  3 2012 Lennart Poettering <lpoetter@redhat.com> - 194-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=859614
- https://bugzilla.redhat.com/show_bug.cgi?id=859655

* Fri Sep 28 2012 Lennart Poettering <lpoetter@redhat.com> - 193-1
- New upstream release

* Tue Sep 25 2012 Lennart Poettering <lpoetter@redhat.com> - 192-1
- New upstream release

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-2
- Fix journal mmap header prototype definition to fix compilation on 32bit

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-1
- New upstream release
- Enable all display managers by default, as discussed with Adam Williamson

* Thu Sep 20 2012 Lennart Poettering <lpoetter@redhat.com> - 190-1
- New upstream release
- Take possession of /etc/localtime, and remove /etc/sysconfig/clock
- https://bugzilla.redhat.com/show_bug.cgi?id=858780
- https://bugzilla.redhat.com/show_bug.cgi?id=858787
- https://bugzilla.redhat.com/show_bug.cgi?id=858771
- https://bugzilla.redhat.com/show_bug.cgi?id=858754
- https://bugzilla.redhat.com/show_bug.cgi?id=858746
- https://bugzilla.redhat.com/show_bug.cgi?id=858266
- https://bugzilla.redhat.com/show_bug.cgi?id=858224
- https://bugzilla.redhat.com/show_bug.cgi?id=857670
- https://bugzilla.redhat.com/show_bug.cgi?id=856975
- https://bugzilla.redhat.com/show_bug.cgi?id=855863
- https://bugzilla.redhat.com/show_bug.cgi?id=851970
- https://bugzilla.redhat.com/show_bug.cgi?id=851275
- https://bugzilla.redhat.com/show_bug.cgi?id=851131
- https://bugzilla.redhat.com/show_bug.cgi?id=847472
- https://bugzilla.redhat.com/show_bug.cgi?id=847207
- https://bugzilla.redhat.com/show_bug.cgi?id=846483
- https://bugzilla.redhat.com/show_bug.cgi?id=846085
- https://bugzilla.redhat.com/show_bug.cgi?id=845973
- https://bugzilla.redhat.com/show_bug.cgi?id=845194
- https://bugzilla.redhat.com/show_bug.cgi?id=845028
- https://bugzilla.redhat.com/show_bug.cgi?id=844630
- https://bugzilla.redhat.com/show_bug.cgi?id=839736
- https://bugzilla.redhat.com/show_bug.cgi?id=835848
- https://bugzilla.redhat.com/show_bug.cgi?id=831740
- https://bugzilla.redhat.com/show_bug.cgi?id=823485
- https://bugzilla.redhat.com/show_bug.cgi?id=821813
- https://bugzilla.redhat.com/show_bug.cgi?id=807886
- https://bugzilla.redhat.com/show_bug.cgi?id=802198
- https://bugzilla.redhat.com/show_bug.cgi?id=767795
- https://bugzilla.redhat.com/show_bug.cgi?id=767561
- https://bugzilla.redhat.com/show_bug.cgi?id=752774
- https://bugzilla.redhat.com/show_bug.cgi?id=732874
- https://bugzilla.redhat.com/show_bug.cgi?id=858735

* Thu Sep 13 2012 Lennart Poettering <lpoetter@redhat.com> - 189-4
- Don't pull in pkg-config as dep
- https://bugzilla.redhat.com/show_bug.cgi?id=852828

* Wed Sep 12 2012 Lennart Poettering <lpoetter@redhat.com> - 189-3
- Update preset policy
- Rename preset policy file from 99-default.preset to 90-default.preset so that people can order their own stuff after the Fedora default policy if they wish

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-2
- Update preset policy
- https://bugzilla.redhat.com/show_bug.cgi?id=850814

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-1
- New upstream release

* Thu Aug 16 2012 Ray Strode <rstrode@redhat.com> 188-4
- more scriptlet fixes
  (move dm migration logic to %%posttrans so the service
   files it's looking for are available at the time
   the logic is run)

* Sat Aug 11 2012 Lennart Poettering <lpoetter@redhat.com> - 188-3
- Remount file systems MS_PRIVATE before switching roots
- https://bugzilla.redhat.com/show_bug.cgi?id=847418

* Wed Aug 08 2012 Rex Dieter <rdieter@fedoraproject.org> - 188-2
- fix scriptlets

* Wed Aug  8 2012 Lennart Poettering <lpoetter@redhat.com> - 188-1
- New upstream release
- Enable gdm and avahi by default via the preset file
- Convert /etc/sysconfig/desktop to display-manager.service symlink
- Enable hardened build

* Mon Jul 30 2012 Kay Sievers <kay@redhat.com> - 187-3
- Obsolete: system-setup-keyboard

* Wed Jul 25 2012 Kalev Lember <kalevlember@gmail.com> - 187-2
- Run ldconfig for the new -libs subpackage

* Thu Jul 19 2012 Lennart Poettering <lpoetter@redhat.com> - 187-1
- New upstream release

* Mon Jul 09 2012 Harald Hoyer <harald@redhat.com> 186-2
- fixed dracut conflict version

* Tue Jul  3 2012 Lennart Poettering <lpoetter@redhat.com> - 186-1
- New upstream release

* Fri Jun 22 2012 Nils Philippsen <nils@redhat.com> - 185-7.gite7aee75
- add obsoletes/conflicts so multilib systemd -> systemd-libs updates work

* Thu Jun 14 2012 Michal Schmidt <mschmidt@redhat.com> - 185-6.gite7aee75
- Update to current git

* Wed Jun 06 2012 Kay Sievers - 185-5.gita2368a3
- disable plymouth in configure, to drop the .wants/ symlinks

* Wed Jun 06 2012 Michal Schmidt <mschmidt@redhat.com> - 185-4.gita2368a3
- Update to current git snapshot
  - Add systemd-readahead-analyze
  - Drop upstream patch
- Split systemd-libs
- Drop duplicate doc files
- Fixed License headers of subpackages

* Wed Jun 06 2012 Ray Strode <rstrode@redhat.com> - 185-3
- Drop plymouth files
- Conflict with old plymouth

* Tue Jun 05 2012 Kay Sievers - 185-2
- selinux udev labeling fix
- conflict with older dracut versions for new udev file names

* Mon Jun 04 2012 Kay Sievers - 185-1
- New upstream release
  - udev selinux labeling fixes
  - new man pages
  - systemctl help <unit name>

* Thu May 31 2012 Lennart Poettering <lpoetter@redhat.com> - 184-1
- New upstream release

* Thu May 24 2012 Kay Sievers <kay@redhat.com> - 183-1
- New upstream release including udev merge.

* Wed Mar 28 2012 Michal Schmidt <mschmidt@redhat.com> - 44-4
- Add triggers from Bill Nottingham to correct the damage done by
  the obsoleted systemd-units's preun scriptlet (#807457).

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

* Fri Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
