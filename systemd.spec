#global gitcommit f01de96

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
Version:        216
Release:        9%{?gitcommit:.git%{gitcommit}}%{?dist}
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
Source2:        99-default-disable.preset
Source3:        85-display-manager.preset
# Prevent accidental removal of the systemd package
Source4:        yum-protect-systemd.conf
Source5:        inittab

# Patch series is available from http://cgit.freedesktop.org/systemd/systemd-stable/log/?h=v215-stable
# GIT_DIR=~/src/systemd/.git git format-patch-ab -M -N --no-signature v216..master
# i=1; for p in 0*patch;do printf "Patch%04d:      %s\n" $i $p; ((i++));done
Patch0001:      0001-systemctl-fail-in-the-case-that-no-unit-files-were-f.patch
Patch0002:      0002-build-remove-repeated-KMOD-section.patch
Patch0003:      0003-machine-id-setup-don-t-try-to-read-UUID-from-VM-cont.patch
Patch0004:      0004-resolved-dns-rr-fix-typo.patch
Patch0005:      0005-resolved-fix-which-return-codes-we-check.patch
Patch0006:      0006-journal-remote-remove-unreachable-code.patch
Patch0007:      0007-util-return-after-freeing-all-members-of-array.patch
Patch0008:      0008-journal-upload-make-sure-that-r-is-initialized.patch
Patch0009:      0009-resolved-write-resolv.conf-search-switch-arguments.patch
Patch0010:      0010-sd-event-add-API-to-access-epoll_fd.patch
Patch0011:      0011-journalctl-add-t-identifier-STRING-option.patch
Patch0012:      0012-CODING_STYLE-document-that-we-don-t-break-lines-at-8.patch
Patch0013:      0013-util-change-return-value-of-startswith-to-non-const.patch
Patch0014:      0014-util-simplify-close_nointr-a-bit.patch
Patch0015:      0015-util-make-asynchronous_close-really-work-like-an-asy.patch
Patch0016:      0016-core-unify-how-we-generate-the-prefix-string-when-du.patch
Patch0017:      0017-service-asynchronous_close-already-checks-for-negati.patch
Patch0018:      0018-service-remove-some-pointless-linebreaks-to-make-thi.patch
Patch0019:      0019-service-don-t-invoke-functions-at-the-same-time-as-d.patch
Patch0020:      0020-service-strv-introduce-strv_find_startswith-and-make.patch
Patch0021:      0021-manager-reuse-sockaddr_union-instead-of-redefining-o.patch
Patch0022:      0022-manager-don-t-dispatch-sd_notify-messages-and-SIGCHL.patch
Patch0023:      0023-core-allow-informing-systemd-about-service-status-ch.patch
Patch0024:      0024-notify-send-STOPPING-1-from-our-daemons.patch
Patch0025:      0025-update-TODO.patch
Patch0026:      0026-bus-when-terminating-our-bus-actviated-services-that.patch
Patch0027:      0027-execute-explain-in-a-comment-why-close_all_fds-is-in.patch
Patch0028:      0028-service-use-the-right-timeout-for-stop-processes-we-.patch
Patch0029:      0029-update-TODO.patch
Patch0030:      0030-service-allow-services-of-Type-oneshot-that-specify-.patch
Patch0031:      0031-install-simplify-usage-of-_cleanup_-macros.patch
Patch0032:      0032-systemctl-in-list-unit-files-always-show-legend-even.patch
Patch0033:      0033-update-TODO.patch
Patch0034:      0034-dbus1-generator-properly-free-the-FILE.patch
Patch0035:      0035-shared-add-MAXSIZE-and-use-it-in-resolved.patch
Patch0036:      0036-missing.h-add-fake-__NR_memfd_create-for-MIPS.patch
Patch0037:      0037-missing.h-add-a-cpp-warning-for-__NR_memfd_create-on.patch
Patch0038:      0038-core-add-support-for-a-configurable-system-wide-star.patch
Patch0039:      0039-core-print-startup-finished-messages-even-if-we-log-.patch
Patch0040:      0040-resolved-fix-typo-in-log-message.patch
Patch0041:      0041-core-introduce-poweroff-as-new-failure-action-types.patch
Patch0042:      0042-core-split-up-starting-manager-state-into-initializi.patch
Patch0043:      0043-update-TODO.patch
Patch0044:      0044-systemctl-fix-broken-list-unit-files-with-root.patch
Patch0045:      0045-sd-event-split-run-into-prepare-wait-dispatch.patch
Patch0046:      0046-sd-event-sd_event_prepare-stay-in-PREPARED-if-sd_eve.patch
Patch0047:      0047-update-TODO.patch
Patch0048:      0048-Revert-systemctl-fix-broken-list-unit-files-with-roo.patch
Patch0049:      0049-udev-hwdb-do-not-look-at-usb_device-parents.patch
Patch0050:      0050-update-TODO.patch
Patch0051:      0051-NEWS-Fix-typos.patch
Patch0052:      0052-missing-add-BPF_XOR.patch
Patch0053:      0053-networkd-wait-online-add-missing-short-option-i-to-o.patch
Patch0054:      0054-test-compress-make-sure-asserts-with-side-effects-us.patch
Patch0055:      0055-test-path-util-use-assert_se-in-all-assertions.patch
Patch0056:      0056-test-util-use-assert_se-for-call-to-safe_mkdir-with-.patch
Patch0057:      0057-sd-bus-remove-unused-call-bus_kernel_create_monitor.patch
Patch0058:      0058-systemctl-Correct-error-message-printed-when-bus_pro.patch
Patch0059:      0059-sd-bus-don-t-include-internal-header-memfd.h-in-publ.patch
Patch0060:      0060-util-make-sure-reset_all_signal_handlers-continues-w.patch
Patch0061:      0061-util-reset-signals-when-we-fork-off-agents.patch
Patch0062:      0062-util-make-use-of-newly-added-reset_signal_mask-call-.patch
Patch0063:      0063-sd-journal-never-log-anything-by-default-from-a-libr.patch
Patch0064:      0064-logind-add-HandleLidSwitchDocked-option-to-logind.co.patch
Patch0065:      0065-units-order-systemd-fsck-.service-after-local-fs-pre.patch
Patch0066:      0066-hibernate-resume-add-a-tool-to-write-a-device-node-s.patch
Patch0067:      0067-hibernate-resume-generator-add-a-generator-for-insta.patch
Patch0068:      0068-man-reword-sd-hibernate-resume-description-and-add-l.patch
Patch0069:      0069-Document-.-.-udev-match-syntax.patch
Patch0070:      0070-po-update-Polish-translation.patch
Patch0071:      0071-keymap-Adjust-for-more-Samsung-900X4-series.patch
Patch0072:      0072-systemctl-fix-broken-list-unit-files-with-root.patch
Patch0073:      0073-tmpfiles-make-resolv.conf-entry-conditional-on-resol.patch
Patch0074:      0074-TODO.patch
Patch0075:      0075-shared-drop-UNIQUE.patch
Patch0076:      0076-shared-make-container_of-use-unique-variable-names.patch
Patch0077:      0077-login-fix-memory-leak-on-DropController.patch
Patch0078:      0078-udev-add-missing-new-line-in-udevadm-error.patch
Patch0079:      0079-util-make-lookup_uid-global.patch
Patch0080:      0080-bus-split-bus_map_all_properties-into-multiple-helpe.patch
Patch0081:      0081-terminal-add-system-view-interface.patch
Patch0082:      0082-terminal-add-input-interface.patch
Patch0083:      0083-terminal-add-evdev-elements-to-idev.patch
Patch0084:      0084-terminal-add-xkb-based-keyboard-devices-to-idev.patch
Patch0085:      0085-terminal-add-systemd-evcat-input-debugging-tool.patch
Patch0086:      0086-man-add-sample-glib-sd-event-integration.patch
Patch0087:      0087-util-fix-minimal-race-where-we-might-miss-SIGTERMs-w.patch
Patch0088:      0088-update-TODO.patch
Patch0089:      0089-terminal-remove-unused-variable.patch
Patch0090:      0090-sd-journal-properly-convert-object-size-on-big-endia.patch
Patch0091:      0091-sd-journal-verify-that-object-start-with-the-field-n.patch
Patch0092:      0092-terminal-sysview-don-t-return-uninitialized-error-co.patch
Patch0093:      0093-nspawn-fix-network-interface.patch
Patch0094:      0094-terminal-free-xkb-state-on-keyboard-destruction.patch
Patch0095:      0095-terminal-free-sysview-device-names-on-destruction.patch
Patch0096:      0096-bus-fix-use-after-free-in-slot-release.patch
Patch0097:      0097-macro-use-unique-variable-names-for-math-macros.patch
Patch0098:      0098-use-the-switch_root-function-in-shutdown.patch
Patch0099:      0099-locale-fix-sending-PropertiesChanged-for-x11-keymap-.patch
Patch0100:      0100-bus-don-t-skip-interfaces-in-bus_message_map_propert.patch
Patch0101:      0101-networkctl-do-not-mix-dns-and-ntp-servers.patch
Patch0102:      0102-update-TODO.patch
Patch0103:      0103-hibernate-resume-refuse-to-run-outside-of-an-initrd.patch
Patch0104:      0104-sd-rtnl-log-if-kernel-buffer-is-overrun-as-we-curren.patch
Patch0105:      0105-sd-event-allow-naming-event-sources.patch
Patch0106:      0106-sd-event-use-event-source-name-rather-than-address-i.patch
Patch0107:      0107-sd-event-name-event-sources-used-in-libraries.patch
Patch0108:      0108-sd-event-simplify-sd_event_source_set_name.patch
Patch0109:      0109-systemd-firstboot.service-fix-man-page-section.patch
Patch0110:      0110-systemd-firstboot-fix-typo-in-man-page.patch
Patch0111:      0111-systemd-journal-upload-fix-invalid-After.patch
Patch0112:      0112-Fix-a-few-typos-in-log-messages.patch
Patch0113:      0113-timesyncd-check-if-stratum-is-valid.patch
Patch0114:      0114-timesyncd-fix-calculation-of-transmit-time.patch
Patch0115:      0115-timesyncd-get-kernel-timestamp-in-nanoseconds.patch
Patch0116:      0116-timesyncd-check-root-distance.patch
Patch0117:      0117-Update-Russian-translation.patch
Patch0118:      0118-completion-filter-templates-from-restartable-units.patch
Patch0119:      0119-udev-remove-userspace-firmware-loading-support.patch
Patch0120:      0120-udev-bump-event-timeout-to-60-seconds.patch
Patch0121:      0121-libudev-fix-symbol-version-for-udev_queue_flush-and-.patch
Patch0122:      0122-Update-french-translation.patch
Patch0123:      0123-Fix-a-few-more-typos.patch
Patch0124:      0124-sd-ipv4ll-name-the-correct-source.patch
Patch0125:      0125-journal-compress-use-LZ4_compress_continue.patch
Patch0126:      0126-test-compress-also-test-with-incompressible-inputs.patch
Patch0127:      0127-systemd-fix-error-message.patch
Patch0128:      0128-cgroup-util-shorten-cg_path_get_session.patch
Patch0129:      0129-test-dhcp6-client-Fix-option-length.patch
Patch0130:      0130-sd-dhcp6-client-properly-calculate-buffer-size-when-.patch
Patch0131:      0131-timesyncd-manager-don-t-clear-current_server_name-if.patch
Patch0132:      0132-units-make-emergency.service-conflict-with-rescue.se.patch
Patch0133:      0133-units-m4-is-not-needed-for-rescue.service.patch
Patch0134:      0134-units-update-rescue.service-and-emergency.service.patch
Patch0135:      0135-Quote-unit-names-in-suggested-systemctl-commandlines.patch
Patch0136:      0136-journalctl-Allow-to-disable-line-cap-with-lines-all.patch
Patch0137:      0137-missing-add-IFF_MULTI_QUEUE.patch
Patch0138:      0138-test-network-fix-off-by-one-error-in-test.patch
Patch0139:      0139-journal-remote-fix-check-if-realloc-failed.patch
Patch0140:      0140-config-parser-fix-mem-leak.patch
Patch0141:      0141-login-fix-mem-leak.patch
Patch0142:      0142-login-simplify-controller-handling.patch
Patch0143:      0143-rules-remove-firmware-loading-rules.patch
Patch0144:      0144-sd-rtnl-don-t-assign-to-unused-variable.patch
Patch0145:      0145-timesyncd-wait-before-reconnecting-to-first-server.patch
Patch0146:      0146-timesyncd-remove-retry_timer-logic-which-is-covered-.patch
Patch0147:      0147-timesyncd-allow-two-missed-replies-before-reselectin.patch
Patch0148:      0148-timesyncd-don-t-reset-polling-interval-when-reselect.patch
Patch0149:      0149-Revert-timesyncd-remove-retry_timer-logic-which-is-c.patch
Patch0150:      0150-man-fix-file-extension-in-udev-rules-example.patch
Patch0151:      0151-base_filesystem_create-do-not-try-to-create-root-if-.patch
Patch0152:      0152-initrd-parse-etc.service-ignore-return-code-of-daemo.patch
Patch0153:      0153-update-TODO.patch
Patch0154:      0154-base-file-system-always-generate-error-messages-loca.patch
Patch0155:      0155-update-TODO.patch
Patch0156:      0156-man-two-fixes-reported-on-irc-by-wget.patch
Patch0157:      0157-build-sys-configure-option-to-disable-hibernation.patch
Patch0158:      0158-localed-double-free-in-error-path-and-modernization.patch
Patch0159:      0159-localed-remove-free_and_copy.patch
Patch0160:      0160-localed-log-locale-keymap-changes-in-detail.patch
Patch0161:      0161-localed-introduce-helper-function-to-simplify-matchi.patch
Patch0162:      0162-localed-check-for-partially-matching-converted-keyma.patch
Patch0163:      0163-systemd-fix-argument-ordering-in-UnsetAndSetEnvironm.patch
Patch0164:      0164-man-fix-typo.patch
Patch0165:      0165-Update-TODO.patch
Patch0166:      0166-networkd-move-carrier-gained-lost-handling-from-link.patch
Patch0167:      0167-networkd-link-save-link-flags-when-the-link-is-added.patch
Patch0168:      0168-networkd-link-do-not-manage-loopback-links.patch
Patch0169:      0169-networkd-link-clarify-log-message-when-receiving-add.patch
Patch0170:      0170-build-don-t-install-busname-units-and-target-if-kdbu.patch
Patch0171:      0171-networkd-link-allow-loopback-links-to-be-manage-but-.patch
Patch0172:      0172-hibernate-resume-let-s-move-all-hibernate-resume-too.patch
Patch0173:      0173-man-make-it-more-clear-that-the-concepts-systemctl-1.patch
Patch0174:      0174-exec-factor-out-most-function-arguments-of-exec_spaw.patch
Patch0175:      0175-exec-move-code-executed-after-fork-into-exec_child.patch
Patch0176:      0176-exit-status-fix-URL-in-comment.patch
Patch0177:      0177-update-TODO.patch
Patch0178:      0178-man-fix-references-to-systemctl-man-page-which-is-no.patch
Patch0179:      0179-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch0180:      0180-bus-factor-out-bus-policy-items.patch
Patch0181:      0181-bus-add-kdbus-endpoint-types.patch
Patch0182:      0182-bus-add-code-to-create-custom-endpoints-and-set-thei.patch
Patch0183:      0183-bus-parse-BusPolicy-directive-in-service-files.patch
Patch0184:      0184-namespace-add-support-for-custom-kdbus-endpoint.patch
Patch0185:      0185-exit-status-add-new-exit-code-for-custom-endpoint-er.patch
Patch0186:      0186-service-hook-up-custom-endpoint-logic.patch
Patch0187:      0187-networkd-tuntap-return-correct-error-when-dev-net-tu.patch
Patch0188:      0188-networkd-netdev-failing-to-create-a-netdev-is-not-fa.patch
Patch0189:      0189-units-networkd-order-after-udev.patch
Patch0190:      0190-networkd-add-preferred-source-to-dhcp4-gateway-route.patch
Patch0191:      0191-TODO.patch
Patch0192:      0192-sd-network-add-_get_network_file-api.patch
Patch0193:      0193-networkctl-show-the-network-file-applied-to-each-lin.patch
Patch0194:      0194-udev-net_setup_link-export-the-.link-filename-applie.patch
Patch0195:      0195-udev-link-config-only-set-name-on-success.patch
Patch0196:      0196-networkctl-show-the-link-file-applied-to-each-link.patch
Patch0197:      0197-networkd-allow-specification-of-DHCP-route-metric.patch
Patch0198:      0198-machined-remove-redundant-sd_notify.patch
Patch0199:      0199-rules-net-setup-link-preserve-ID_NET_LINK_FILE-and-I.patch
Patch0200:      0200-rules-net-setup-link-remove-stray-linebreak.patch
Patch0201:      0201-namespace-avoid-posible-use-of-uninitialized-variabl.patch
Patch0202:      0202-execute-silence-warnings.patch
Patch0203:      0203-hwdb-update.patch
Patch0204:      0204-build-sys-make-hibernation-support-configure-option-.patch
Patch0205:      0205-udev-import-the-full-db-on-MOVE-events-for-devices-w.patch
Patch0206:      0206-udev-event-keep-one-rtnl-per-worker-rather-than-per-.patch
Patch0207:      0207-udev-net_setup_link-open-ethtool-and-rtnl-connection.patch
Patch0208:      0208-udev-netif_rename-don-t-log-to-kmsg.patch
Patch0209:      0209-udev-drop-print_kmsg.patch
Patch0210:      0210-sd-dhcp6-client-Implement-Elapsed-Time-option.patch
Patch0211:      0211-test-dhcp6-client-Add-checks-for-Elapsed-Time-option.patch
Patch0212:      0212-TODO-Remove-Elapsed-Time-DHCPv6-option-as-it-is-done.patch
Patch0213:      0213-udev-fix-copy-paste-error-in-log-message.patch
Patch0214:      0214-udev-timeout-increase-timeout.patch
Patch0215:      0215-backlight-Avoid-error-when-state-restore-is-disabled.patch
Patch0216:      0216-terminal-discard-async-read-errors-for-evdev.patch
Patch0217:      0217-terminal-remove-redundant-struct-prefixes.patch
Patch0218:      0218-udev-allow-removing-tags-via-TAG-foobar.patch
Patch0219:      0219-terminal-remove-unused-set.h-inclusion-in-idev.patch
Patch0220:      0220-terminal-enable-sessions-in-evcat-after-taking-contr.patch
Patch0221:      0221-terminal-fix-wrong-return-value-in-idev-if-fcntl-fai.patch
Patch0222:      0222-terminal-drop-redundant-assertion.patch
Patch0223:      0223-bus-avoid-using-m-kdbus-after-freeing-it.patch
Patch0224:      0224-journal-do-not-dereference-already-freed-patterns.patch
Patch0225:      0225-terminal-fix-uninitialized-variable-in-strerror-log-.patch
Patch0226:      0226-journal-do-not-leak-mmaps-on-OOM.patch
Patch0227:      0227-bus-unref-buscreds-on-failure.patch
Patch0228:      0228-test-fix-mem-leak-in-fdopen-test.patch
Patch0229:      0229-activate-fix-fd-leak-in-do_accept.patch
Patch0230:      0230-manager-use-correct-cleanup-function.patch
Patch0231:      0231-firstboot-silence-a-warning.patch
Patch0232:      0232-udev-timeout-warn-after-a-third-of-the-timeout-befor.patch
Patch0233:      0233-analyze-avoid-a-null-dereference.patch
Patch0234:      0234-core-smack-setup-Actually-allow-for-succesfully-load.patch
Patch0235:      0235-analyze-fix-mem-leak.patch
Patch0236:      0236-core-fix-a-potential-mem-leak.patch
Patch0237:      0237-core-use-correct-function-to-free-CalendarSpec.patch
Patch0238:      0238-networkd-remove-vestigial-event-sources.patch
Patch0239:      0239-resolved-fall-back-to-hardcoded-ifindex-when-checkin.patch
Patch0240:      0240-sd-dhcp-fix-test-of-magic-cookie.patch
Patch0241:      0241-test-fix-test-of-uid-range.patch
Patch0242:      0242-build-colorize-gcc-only-if-on-tty.patch
Patch0243:      0243-hashmap-introduce-hash_ops-to-make-struct-Hashmap-sm.patch
Patch0244:      0244-hashmap-set-remove-unused-functions.patch
Patch0245:      0245-hashmap-minor-hashmap_replace-optimization.patch
Patch0246:      0246-sd-bus-use-proper-ITERATOR_FIRST-abstraction.patch
Patch0247:      0247-remove-unneeded-error.h-includes.patch
Patch0248:      0248-terminal-fix-missing-hashmap_new-conversions.patch
Patch0249:      0249-man-sd_bus_error-typo-fix.patch
Patch0250:      0250-udev-split-out-help-and-modernise-a-bit.patch
Patch0251:      0251-udev-split-out-parse_argv.patch
Patch0252:      0252-udev-drop-duplicate-logging.patch
Patch0253:      0253-udev-don-t-close-std-in-out-err.patch
Patch0254:      0254-udevd-initialize-epoll_event-structs-on-allocation.patch
Patch0255:      0255-udev-only-print-after-final-log-level-has-been-deter.patch
Patch0256:      0256-udev-apply-permissions-to-static-nodes-before-signal.patch
Patch0257:      0257-libudev-drop-util_lookup_-user-group.patch
Patch0258:      0258-libudev-util-drop-util_delete_path.patch
Patch0259:      0259-udev-util-use-log_level_from_string.patch
Patch0260:      0260-udevd-use-safe_ato-in-place-of-strto.patch
Patch0261:      0261-udev-rules-add-missing-whitespace-to-log-message.patch
Patch0262:      0262-gpt-auto-generator-fix-typo.patch
Patch0263:      0263-libsystemd-network-avoid-double-free-in-error-case.patch
Patch0264:      0264-hostname-add-missing-EMITS_CHANGE-annotation.patch
Patch0265:      0265-bootchart-use-safe_atod-rather-than-strtod.patch
Patch0266:      0266-bootchart-oom-check-correct-variable.patch
Patch0267:      0267-sd-bus-sd_bus_message_get_errno-should-only-return-p.patch
Patch0268:      0268-terminal-sd_bus_error_get_errno-returns-positive-err.patch
Patch0269:      0269-missing-memfd_create-takes-unsigned-int-flags-in-fin.patch
Patch0270:      0270-core-fix-resource-leak-in-manager_environment_add.patch
Patch0271:      0271-sysv-generator-fix-resource-leak.patch
Patch0272:      0272-shared-fix-resource-leak-in-config_parse_default_ins.patch
Patch0273:      0273-test-silence-a-coverity-report.patch
Patch0274:      0274-terminal-remove-dead-code-checking-O_WRONLY.patch
Patch0275:      0275-util-remove-a-unnecessary-check.patch
Patch0276:      0276-sysctl-make-prefix-allow-all-kinds-of-sysctl-paths.patch
Patch0277:      0277-bus-never-respond-to-GetManagedObjects-on-sub-paths.patch
Patch0278:      0278-bus-fix-error-leak-in-bus_node_exists.patch
Patch0279:      0279-networkd-dhcp4-fix-unchecked-return-value.patch
Patch0280:      0280-libsystemd-network-dhcp-test-assert-that-malloc0-suc.patch
Patch0281:      0281-udev-rules-close-empty-file.patch
Patch0282:      0282-nss-resolve-remove-dead-code.patch
Patch0283:      0283-udev-event-modernize-spawn_read.patch
Patch0284:      0284-udev-event-explicitly-don-t-read-from-invalid-fd.patch
Patch0285:      0285-udev-event-modernize-spawn_exec.patch
Patch0286:      0286-shared-conf-parser.patch
Patch0287:      0287-logind-fix-typo.patch
Patch0288:      0288-sysv-generator-don-t-check-first-if-hashmap-contains.patch
Patch0289:      0289-Fix-resource-leak-coverity-CID-1237760.patch
Patch0290:      0290-systemctl-fix-resource-leak-CID-1237747.patch
Patch0291:      0291-sd-bus-sync-kdbus.h.patch
Patch0292:      0292-tests-fix-resource-mem-leaks.patch
Patch0293:      0293-libudev-monitor-warn-if-we-fail-to-request-SO_PASSCR.patch
Patch0294:      0294-shared-conf-parser-don-t-leak-memory-on-error-in-DEF.patch
Patch0295:      0295-bus-fix-bus_print_property-to-use-int-for-booleans.patch
Patch0296:      0296-udev-fix-path-for-database-names-on-change-event.patch
Patch0297:      0297-man-use-the-escape-for-in-example-instead-of-space.patch
Patch0298:      0298-journal-Do-not-count-on-the-compiler-initializing-fo.patch
Patch0299:      0299-udev-link-config-remove-unneded-linux-netdevice.h-in.patch
Patch0300:      0300-sd-rtnl-rtnl-message-remove-unneeded-linux-includes.patch
Patch0301:      0301-include-fcntl.h-rather-than-sys-fcntl.h.patch
Patch0302:      0302-mount-order-options-before-other-arguments-to-mount.patch
Patch0303:      0303-journal-upload-Remove-compilation-warning.patch
Patch0304:      0304-core-Remove-uninitialized-warnings-from-bus-endpoint.patch
Patch0305:      0305-sysusers-Remove-some-gcc-warnings-about-uninitialize.patch
Patch0306:      0306-journal-remote-check-return-code-of-sd_event_default.patch
Patch0307:      0307-udevd-parse_argv-warn-if-argumens-are-invalid.patch
Patch0308:      0308-udevd-check-return-of-various-functions.patch
Patch0309:      0309-udevadm-hwdb-check-return-value-of-fseeko.patch
Patch0310:      0310-udev-node-warn-if-chmod-chown-fails.patch
Patch0311:      0311-udev-ctrl-log-if-setting-SO_PASSCRED-fails.patch
Patch0312:      0312-udev-fix-typos.patch
Patch0313:      0313-udevd-don-t-fail-if-run-udev-exists.patch
Patch0314:      0314-timesyncd-check-return-of-setting-IP_TOS.patch
Patch0315:      0315-nss-remove-dead-code.patch
Patch0316:      0316-pty-include-linux-ioctl.h-for-TIOCSIG.patch
Patch0317:      0317-shared-label.h-add-missing-stdio.h-include.patch
Patch0318:      0318-shared-sparse-endian.h-add-missing-byteswap.h-includ.patch
Patch0319:      0319-test-warn-if-we-could-not-parse-the-loop-count-argum.patch
Patch0320:      0320-shared-wtmp-utmp-don-t-clear-store_wtmp-in-utmp_put_.patch
Patch0321:      0321-socket-introduce-SELinuxContextFromNet-option.patch
Patch0322:      0322-login-pause-devices-before-acknowledging-VT-switches.patch
Patch0323:      0323-terminal-add-graphics-interface.patch
Patch0324:      0324-terminal-add-grdev-DRM-backend.patch
Patch0325:      0325-terminal-add-systemd-modeset-debugging-tool.patch
Patch0326:      0326-nspawn-don-t-try-to-create-veth-link-with-too-long-i.patch
Patch0327:      0327-terminal-parse-ID_SEAT-not-only-for-parents-but-the-.patch
Patch0328:      0328-terminal-forward-DEVICE_CHANGE-events-via-sysview.patch
Patch0329:      0329-terminal-make-drm-connectors-first-level-devices.patch
Patch0330:      0330-terminal-reduce-speed-of-morphing-colors-in-modeset-.patch
Patch0331:      0331-terminal-modeset-forward-DEVICE_CHANGE-events-into-g.patch
Patch0332:      0332-terminal-grdev-treat-udev-devices-without-devnum-as-.patch
Patch0333:      0333-terminal-grdev-refresh-device-state-on-hotplug-event.patch
Patch0334:      0334-terminal-split-grdrm_crtc_commit-apart.patch
Patch0335:      0335-terminal-grdev-raise-frame-event-after-DISPLAY_ADD-C.patch
Patch0336:      0336-terminal-grdev-schedule-virtual-frame-events-if-hw-d.patch
Patch0337:      0337-terminal-restructure-some-logging-calls-in-grdrm.patch
Patch0338:      0338-terminal-fix-mode-sync-for-connectors.patch
Patch0339:      0339-test-udev-restrict-nemuric-uid-s-to-existing-ones.patch
Patch0340:      0340-bus-policy-story-mandatory-items-in-right-list.patch
Patch0341:      0341-bus-policy-append-items-rather-than-prepending-them.patch
Patch0342:      0342-bus_policy-set-i-ug-id_valid.patch
Patch0343:      0343-bus-policy-resolve-ug-id-of-POLICY_ITEM_-USER-GROUP.patch
Patch0344:      0344-bus-policy-implement-dump_items-with-LIST_FOREACH.patch
Patch0345:      0345-bus-policy-do-not-exit-from-policy_dump.patch
Patch0346:      0346-bus-policy-print-numeric-gu-id-in-dump_items.patch
Patch0347:      0347-bus-policy-add-policy-check-function.patch
Patch0348:      0348-bus-policy-add-test-utility.patch
Patch0349:      0349-terminal-print-RESYNC-state-in-evcat.patch
Patch0350:      0350-terminal-always-call-_enable-_disable-on-evdev-devic.patch
Patch0351:      0351-terminal-forward-evdev-RESYNC-events-to-linked-devic.patch
Patch0352:      0352-terminal-raise-sysview-DEVICE_CHANGE-events-per-atta.patch
Patch0353:      0353-test-util-make-valgrind-happy.patch
Patch0354:      0354-util-add-alloca_align.patch
Patch0355:      0355-bus-align-kdbus-ioctl-parameters-to-8byte.patch
Patch0356:      0356-login-add-public-sd_session_get_desktop-API.patch
Patch0357:      0357-man-fix-typo-and-add-link.patch
Patch0358:      0358-exit-status.c-bring-EXIT_BUS_ENDPOINT-label-in-line-.patch
Patch0359:      0359-terminal-make-evdev-logind-matches-per-session.patch
Patch0360:      0360-terminal-allow-user-context-to-be-retrieved-stored.patch
Patch0361:      0361-terminal-handle-callback-errors-in-sysview-instead-o.patch
Patch0362:      0362-terminal-signal-object-removal-during-sysview_contex.patch
Patch0363:      0363-util-avoid-non-portable-__WORDSIZE.patch
Patch0364:      0364-sd-bus-sync-kdbus.h-API-ABI-break.patch
Patch0365:      0365-logind-add-support-for-Triton2-Power-Button.patch
Patch0366:      0366-terminal-fix-spelling-mistake.patch
Patch0367:      0367-Fix-warning-about-unused-variable-with-SELINUX.patch
Patch0368:      0368-localed-rename-write_data_x11-to-x11_write_data.patch
Patch0369:      0369-sd-bus-sync-kdbus.h-API-break.patch
Patch0370:      0370-sd-bus-sync-kdbus.h.patch
Patch0371:      0371-Silence-some-unchecked-return-value-warnings.patch
Patch0372:      0372-terminal-fix-tile-offset-calculation.patch
Patch0373:      0373-terminal-verify-grdev-tiles-are-correctly-linked.patch
Patch0374:      0374-terminal-verify-kernel-returned-DRM-events-are-not-t.patch
Patch0375:      0375-terminal-provide-display-dimensions-to-API-users.patch
Patch0376:      0376-bus-remove-unused-check.patch
Patch0377:      0377-bus-policy-split-API-for-bus-proxyd.patch
Patch0378:      0378-fileio-make-parse_env_file-return-number-of-parsed-i.patch
Patch0379:      0379-localectl-print-warning-when-there-are-options-given.patch
Patch0380:      0380-bus-proxyd-add-some-asserts.patch
Patch0381:      0381-shared-path-util-try-to-make-PATH_FORECH_PREFIX-look.patch
Patch0382:      0382-bus-proxy-drop-one-wrong-assert.patch
# Patch0383:      0383-readahead-wipe-out-readahead.patch
Patch0384:      0384-delta-warn-if-diff-failed.patch
Patch0385:      0385-nspawn-check-some-more-return-values.patch
Patch0386:      0386-journal-remote-initialize-writer-hashmap-before-use.patch
Patch0387:      0387-journal-remote-fix-counting-of-events-written.patch
Patch0388:      0388-journal-build-fix-when-LZ4-is-enabled-but-XZ-is-not.patch
Patch0389:      0389-man-sd_event_new-tweaks.patch
Patch0390:      0390-build-sys-add-sd_session_get_desktop-to-Makefile-man.patch
Patch0391:      0391-man-add-sd_event_add_signal-3.patch
Patch0392:      0392-man-add-sd_event_add_child-3.patch
Patch0393:      0393-man-document-sd_event_add_-defer-post-exit.patch
Patch0394:      0394-man-use-constant-markup-for-errno-value.patch
Patch0395:      0395-only-build-and-install-systemd-bus-proxyd-if-enable-.patch
Patch0396:      0396-build-sys-do-not-distribute-make-man-rules.py.patch
Patch0397:      0397-do-not-install-factory-etc-pam.d-if-disable-pam.patch
Patch0398:      0398-Revert-only-build-and-install-systemd-bus-proxyd-if-.patch
Patch0399:      0399-make-utmp-wtmp-support-configurable.patch
Patch0400:      0400-systemd-tmpfiles-Fix-IGNORE_DIRECTORY_PATH-age-handl.patch
Patch0401:      0401-test-bus-policy-load-policy-files-from-TEST_DIR.patch
Patch0402:      0402-shutdownd-clean-up-initialization-of-struct.patch
Patch0403:      0403-shell-completion-zsh-journalctl-s-b-changes.patch
Patch0404:      0404-catalog-add-Polish-translation.patch
Patch0405:      0405-logind-add-support-for-TPS65217-Power-Button.patch
Patch0406:      0406-bootchart-parse-userinput-with-safe_atoi.patch
Patch0407:      0407-bootchart-check-return-of-strftime.patch
Patch0408:      0408-test-bus-policy-silence-coverity.patch
Patch0409:      0409-bootchart-Do-not-try-to-access-data-for-non-existing.patch
Patch0410:      0410-sd-bus-clean-up-string-length-calculation.patch
Patch0411:      0411-terminal-add-sysview_seat_switch_to.patch
Patch0412:      0412-bus-sync-kdbus.h-ABI-break.patch
Patch0413:      0413-terminal-add-helper-to-retrieve-the-seat-of-a-sessio.patch
Patch0414:      0414-bus-use-2M-as-maximum-message-size-in-benchmark.patch
Patch0415:      0415-journalctl-do-not-output-reboot-markers-when-running.patch
Patch0416:      0416-journal-remote-fix-handling-of-non-blocking-sources.patch
Patch0417:      0417-swap-introduce-Discard-property.patch
Patch0418:      0418-fstab-generator-properly-deal-with-discard-as-non-la.patch
Patch0419:      0419-core-swap-follow-the-configured-unit-by-default.patch
Patch0420:      0420-core-swap-advertise-Discard-over-dbus.patch
Patch0421:      0421-core-dbus-simplify-handling-of-CPUQuotaPerSecUSec.patch
Patch0422:      0422-Do-not-format-USEC_INFINITY-as-NULL.patch
Patch0423:      0423-nspawn-log-when-tearing-down-of-loop-device-fails.patch
Patch0424:      0424-util-silence-coverity.patch
Patch0425:      0425-udev-hwdb-New-Entry-for-Dell-XPS12-9Q33-keyboard.patch
Patch0426:      0426-core-execute-don-t-leak-strv.patch
Patch0427:      0427-shared-util-use-nicer-idiom-to-silence-Coverity.patch
Patch0428:      0428-vconsole-silence-coverity.patch
Patch0429:      0429-test-path-util-fix-a-mem-leak-and-avoid-confusing-co.patch
Patch0430:      0430-test-date-don-t-fail-test-if-log_max_level-is-higher.patch
Patch0431:      0431-test-fileio-Remove-dead-check.patch
Patch0432:      0432-core-limit-timestamp-to-sane-precision.patch
Patch0433:      0433-tmpfiles-use-allocated-buffer-for-path.patch
Patch0434:      0434-shared-util-use-nicer-idiom-to-silence-Coverity.patch
Patch0435:      0435-tests-add-tests-for-hashmap-set-_steal_first.patch
Patch0436:      0436-gitignore-add-test-set.patch
Patch0437:      0437-Remove-repeated-includes.patch
Patch0438:      0438-core-swap-only-make-configured-units-part-of-swap.ta.patch
Patch0439:      0439-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch0440:      0440-PORTING-DBUS1-we-use-1.-llu-not-0.-llu-for-D-Bus-uni.patch
Patch0441:      0441-sd-bus-use-terms-from-the-D-Bus-Specification-a-bit-.patch
Patch0442:      0442-terminal-move-unifont-internal.h-to-unifont.h.patch
Patch0443:      0443-terminal-add-unifont_get_width-height.patch
Patch0444:      0444-terminal-move-unifont-map-to-datadir.patch
Patch0445:      0445-terminal-add-term.h-header-for-library-users.patch
Patch0446:      0446-terminal-add-helpers-to-retrieve-page-dimensions.patch
Patch0447:      0447-barrier-fix-up-constructor-error-handling.patch
Patch0448:      0448-Correct-a-few-typos.patch
Patch0449:      0449-sd-bus-sync-kdbus.h-ABI-break.patch
Patch0450:      0450-localectl-count-locale-variables-from-0-instead-of-V.patch
Patch0451:      0451-localectl-always-print-warnings-with-log_warning-ins.patch
Patch0452:      0452-journalctl-add-utc-option.patch
Patch0453:      0453-add-a-transient-user-unit-directory.patch
Patch0454:      0454-Rename-user_runtime-to-user_runtime_dir.patch
Patch0455:      0455-Fix-order-and-document-user-unit-dirs.patch
Patch0456:      0456-virt-detect-that-we-are-running-inside-the-docker-co.patch
Patch0457:      0457-sd-bus-sync-kdbus.h-ABI-break.patch
Patch0458:      0458-sd-dhcp6-client-support-custom-DUIDs.patch
Patch0459:      0459-sd-dhcp6-support-custom-DUID-s-up-to-the-size-specif.patch
Patch0460:      0460-sd-dhcp6-specify-the-type-explicitly-when-setting-cu.patch
Patch0461:      0461-sd-dhcp6-do-basic-sanity-checking-of-supplied-DUID.patch
Patch0462:      0462-update-TODO.patch
Patch0463:      0463-kdbus-make-sure-we-never-invoke-free-on-an-uninitial.patch
Patch0464:      0464-kdbus-don-t-clobber-return-values-use-strjoin-instea.patch
Patch0465:      0465-systemctl-remove-spurious-newline.patch
Patch0466:      0466-Revert-mount-order-options-before-other-arguments-to.patch
Patch0467:      0467-firstboot-silence-coverity.patch
Patch0468:      0468-man-add-sd_event_get_fd-3.patch
Patch0469:      0469-man-add-sd_event_set_name-3.patch
Patch0470:      0470-test-barrier-add-checks-after-the-barrier-constructo.patch
Patch0471:      0471-glib-event-glue-remove-some-unnecessary-lines.patch
Patch0472:      0472-man-fix-sd_event_set_name-compilation.patch
Patch0473:      0473-bootchart-use-n-a-if-PRETTY_NAME-is-not-found.patch
Patch0474:      0474-journalctl-make-utc-work-everywhere.patch
Patch0475:      0475-fileio-label-return-error-when-writing-fails.patch
Patch0476:      0476-terminal-fix-back-buffer-selection-on-DRM-page-flip.patch
Patch0477:      0477-terminal-make-utf8-decoder-return-length.patch
Patch0478:      0478-terminal-grdev-simplify-DRM-event-parsing.patch
Patch0479:      0479-terminal-drm-provide-pipe-target-callback.patch
Patch0480:      0480-terminal-grdev-provide-front-and-back-buffer-to-rend.patch
Patch0481:      0481-terminal-grdev-allow-arbitrary-fb-age-contexts.patch
Patch0482:      0482-terminal-drm-clear-applied-flag-when-changing-state.patch
Patch0483:      0483-terminal-add-screen-renderer.patch
Patch0484:      0484-terminal-subterm-use-screen-renderer.patch
Patch0485:      0485-terminal-unifont-add-built-in-fallback-glyph.patch
Patch0486:      0486-terminal-idev-don-t-map-XKB_KEY_NoSymbol-as-ASCII-0.patch
Patch0487:      0487-terminal-screen-add-keyboard-mapping.patch
Patch0488:      0488-terminal-idev-add-helper-to-match-keyboard-shortcuts.patch
Patch0489:      0489-terminal-screen-mark-cursor-dirty-on-enabled-disable.patch
Patch0490:      0490-terminal-screen-add-cursor-rendering.patch
Patch0491:      0491-terminal-screen-add-color-converter.patch
Patch0492:      0492-terminal-screen-adjust-screen-age-only-on-update.patch
Patch0493:      0493-pty-optimize-read-loop.patch
Patch0494:      0494-console-add-user-console-daemon.patch
Patch0495:      0495-man-use-more-markup-in-daemon-7.patch
Patch0496:      0496-sd-event-check-the-value-of-received-signal.patch
Patch0497:      0497-core-namespace-remove-invalid-check.patch
Patch0498:      0498-core-namespace-remove-invalid-check.patch
Patch0499:      0499-sd-bus-split-out-cleanup-into-separate-function.patch
Patch0500:      0500-fstab-generator-Small-cleanup.patch
Patch0501:      0501-sd-id128-do-stricter-checking-of-random-boot-id.patch
Patch0502:      0502-man-say-that-SecureBits-are-space-separated.patch
Patch0503:      0503-build-sys-fix-make-distcheck.patch
Patch0504:      0504-systemd-bus-proxyd-distribute-the-.in-file-also-for-.patch
Patch0505:      0505-consoled-move-from-bin-to-lib-systemd.patch
Patch0506:      0506-consoled-add-a-unit-file.patch
Patch0507:      0507-test-only-use-assert_se.patch
Patch0508:      0508-terminal-fix-restoring-of-screen-flags.patch
Patch0509:      0509-terminal-fix-TERM_FLAG_-comment.patch
Patch0510:      0510-terminal-subterm-skip-setting-parent-s-cursor.patch
Patch0511:      0511-terminal-screen-save-state-in-separate-object.patch
Patch0512:      0512-terminal-screen-add-support-for-alternate-screen-buf.patch
Patch0513:      0513-terminal-subterm-leave-bold-light-conversion-to-pare.patch
Patch0514:      0514-terminal-screen-perform-bold-light-conversion-only-o.patch
Patch0515:      0515-terminal-idev-don-t-remove-consumed-mods-from-kbd-ma.patch
Patch0516:      0516-bus-add-assert-to-check-that-we-re-not-freeing-a-sta.patch
Patch0517:      0517-ask-password-Add-echo-to-enable-echoing-the-user-inp.patch
Patch0518:      0518-Update-TODO.patch
Patch0519:      0519-terminal-remove-an-unused-initialization.patch
Patch0520:      0520-build-sys-use-linux-memfd.h-if-available.patch
Patch0521:      0521-sd-bus-sync-kdbus.h-ABI-break.patch
Patch0522:      0522-sd-bus-remove-unused-variable.patch
Patch0523:      0523-keymap-Fix-touchpad-toggle-on-Toshiba-Satellite-P75-.patch
Patch0524:      0524-keymap-Fix-touchpad-toggle-key-on-Asus-laptops.patch
Patch0525:      0525-sd-bus-fix-use-after-free-in-close_kdbus_msg.patch
Patch0526:      0526-sd-bus-fix-KDBUS_CMD_FREE-user.patch
Patch0527:      0527-sd-bus-check-return-value-of-vasprintf.patch
Patch0528:      0528-bus-proxyd-check-return-values-of-getpeercred-and-ge.patch
Patch0529:      0529-man-move-commandline-parsing-to-a-separate-section.patch
Patch0530:      0530-man-document-stripping-of-quotes.patch
Patch0531:      0531-Update-TODO.patch
Patch0532:      0532-proc-sys-prefixes-are-not-necessary-for-sysctl-anymo.patch
Patch0533:      0533-core-don-t-allow-enabling-if-unit-is-masked.patch
Patch0534:      0534-fedora-disable-resolv.conf-symlink.patch


# kernel-install patch for grubby, drop if grubby is obsolete
Patch1000:      kernel-install-grubby.patch

%global num_patches %{lua: c=0; for i,p in ipairs(patches) do c=c+1; end; print(c);}

BuildRequires:  libcap-devel
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
BuildRequires:  libidn-devel
BuildRequires:  libcurl-devel
BuildRequires:  kmod-devel
BuildRequires:  elfutils-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  gnutls-devel
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
BuildRequires:  python-lxml
BuildRequires:  python3-lxml
# libseccomp is currently explicitly only supported on x86/armv7
%ifarch %{arm} %{ix86} x86_64
# https://bugzilla.redhat.com/show_bug.cgi?id=1071278
# https://bugzilla.redhat.com/show_bug.cgi?id=1073647
# https://bugzilla.redhat.com/show_bug.cgi?id=1071284
BuildRequires:  libseccomp-devel
%endif
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
Requires:       kmod >= 15
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

%package compat-libs
Summary:        systemd compatibility libraries
License:        LGPLv2+ and MIT
# To reduce confusion, this package can only be installed in parallel
# with the normal systemd-libs, same version.
Requires:       systemd-libs = %{version}-%{release}

%description compat-libs
Compatibility libraries for systemd. If your package requires this
package, you need to update your link options and build.

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
Requires:       %{name} = %{version}-%{release}

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
        --exclude src/libsystemd/sd-bus/PORTING-DBUS1 \
        --exclude CODING_STYLE \
        --exclude src/readahead/Makefile \
        --exclude src/libsystemd-terminal/unifont-def.h \
        %{patches}
%endif

%ifarch ppc ppc64 ppc64le
# Disable link warnings, somehow they cause the link to fail.
sed -r -i 's/\blibsystemd-(login|journal|id128|daemon).c \\/\\/' Makefile.am
%endif

%build
%if %{defined gitcommit}
    ./autogen.sh
%else
    %if %{num_patches}
        autoreconf -i
    %endif
%endif

%{?fedora: %global ntpvendor fedora}
%{?rhel:   %global ntpvendor rhel}
%{!?ntpvendor: echo 'NTP vendor zone is not set!'; exit 1}

# first make python3 while source directory is empty
rm -rf build2 build3
mkdir build2
mkdir build3

CONFIGURE_OPTS=(
        --libexecdir=%{_prefix}/lib
        --with-sysvinit-path=/etc/rc.d/init.d
        --with-rc-local-script-path-start=/etc/rc.d/rc.local
        --with-ntp-servers='0.%{ntpvendor}.pool.ntp.org 1.%{ntpvendor}.pool.ntp.org 2.%{ntpvendor}.pool.ntp.org 3.%{ntpvendor}.pool.ntp.org'
        --disable-kdbus
        --disable-terminal
)

pushd build3
%define _configure ../configure
%configure \
        "${CONFIGURE_OPTS[@]}" \
        --disable-manpages \
        --disable-compat-libs \
        PYTHON=%{__python3}
make %{?_smp_mflags} GCC_COLORS="" V=1
popd

pushd build2
%configure \
        "${CONFIGURE_OPTS[@]}" \
        --enable-gtk-doc \
        --enable-compat-libs
make %{?_smp_mflags} GCC_COLORS="" V=1
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
sed -i 's/L+/#/' %{buildroot}/usr/lib/tmpfiles.d/etc.conf

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

# Compatiblity and documentation files
touch %{buildroot}/etc/crypttab
chmod 600 %{buildroot}/etc/crypttab

install -m 0644 %{SOURCE5} %{buildroot}/etc/

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
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Make sure the shutdown/sleep drop-in dirs exist
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-shutdown/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep/

# Make sure directories in /var exist
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/backlight
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/rfkill
mkdir -p %{buildroot}%{_localstatedir}/log/journal
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin
touch %{buildroot}%{_localstatedir}/lib/systemd/random-seed
touch %{buildroot}%{_localstatedir}/lib/systemd/clock

# Install yum protection fragment
mkdir -p %{buildroot}%{_sysconfdir}/yum/protected.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/yum/protected.d/systemd.conf

# Delete LICENSE files from _docdir (we'll get them in as %%license)
rm -rf %{buildroot}%{_docdir}/LICENSE*

%find_lang %{name}

%pre
getent group cdrom >/dev/null 2>&1 || groupadd -r -g 11 cdrom >/dev/null 2>&1 || :
getent group tape >/dev/null 2>&1 || groupadd -r -g 33 tape >/dev/null 2>&1 || :
getent group dialout >/dev/null 2>&1 || groupadd -r -g 18 dialout >/dev/null 2>&1 || :
getent group input >/dev/null 2>&1 || groupadd -r input >/dev/null 2>&1 || :
getent group systemd-journal >/dev/null 2>&1 || groupadd -r -g 190 systemd-journal 2>&1 || :
getent group systemd-timesync >/dev/null 2>&1 || groupadd -r systemd-timesync 2>&1 || :
getent passwd systemd-timesync >/dev/null 2>&1 || useradd -r -l -g systemd-timesync -d / -s /sbin/nologin -c "systemd Time Synchronization" systemd-timesync >/dev/null 2>&1 || :
getent group systemd-network >/dev/null 2>&1 || groupadd -r systemd-network 2>&1 || :
getent passwd systemd-network >/dev/null 2>&1 || useradd -r -l -g systemd-network -d / -s /sbin/nologin -c "systemd Network Management" systemd-network >/dev/null 2>&1 || :
getent group systemd-resolve >/dev/null 2>&1 || groupadd -r systemd-resolve 2>&1 || :
getent passwd systemd-resolve >/dev/null 2>&1 || useradd -r -l -g systemd-resolve -d / -s /sbin/nologin -c "systemd Resolver" systemd-resolve >/dev/null 2>&1 || :
getent group systemd-bus-proxy >/dev/null 2>&1 || groupadd -r systemd-bus-proxy 2>&1 || :
getent passwd systemd-bus-proxy >/dev/null 2>&1 || useradd -r -l -g systemd-bus-proxy -d / -s /sbin/nologin -c "systemd Bus Proxy" systemd-bus-proxy >/dev/null 2>&1 || :

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
chgrp systemd-journal /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :
chmod g+s /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :

# Apply ACL to the journal directory
setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx /var/log/journal/ >/dev/null 2>&1 || :

# Move old stuff around in /var/lib
mv %{_localstatedir}/lib/random-seed %{_localstatedir}/lib/systemd/random-seed >/dev/null 2>&1 || :
mv %{_localstatedir}/lib/backlight %{_localstatedir}/lib/systemd/backlight >/dev/null 2>&1 || :

# Stop-gap until rsyslog.rpm does this on its own. (This is supposed
# to fail when the link already exists)
ln -s /usr/lib/systemd/system/rsyslog.service /etc/systemd/system/syslog.service >/dev/null 2>&1 || :

# Services we install by default, and which are controlled by presets.
if [ $1 -eq 1 ] ; then
        systemctl preset \
                remote-fs.target \
                getty@.service \
                serial-getty@.service \
                console-getty.service \
                console-shell.service \
                debug-shell.service \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                systemd-timesyncd.service \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                >/dev/null 2>&1 || :
fi

# sed-fu to add myhostname to the hosts line of /etc/nsswitch.conf
if [ -f /etc/nsswitch.conf ] ; then
        sed -i.bak -e '
                /^hosts:/ !b
                /\<myhostname\>/ b
                s/[[:blank:]]*$/ myhostname/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
        systemctl daemon-reload > /dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        systemctl disable \
                remote-fs.target \
                getty@.service \
                serial-getty@.service \
                console-getty.service \
                console-shell.service \
                debug-shell.service \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                systemd-timesyncd.service \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                >/dev/null 2>&1 || :

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

%post compat-libs -p /sbin/ldconfig
%postun compat-libs -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%pre journal-gateway
getent group systemd-journal-gateway >/dev/null 2>&1 || groupadd -r -g 191 systemd-journal-gateway 2>&1 || :
getent passwd systemd-journal-gateway >/dev/null 2>&1 || useradd -r -l -u 191 -g systemd-journal-gateway -d %{_localstatedir}/log/journal -s /sbin/nologin -c "Journal Gateway" systemd-journal-gateway >/dev/null 2>&1 || :
getent group systemd-journal-remote >/dev/null 2>&1 || groupadd -r systemd-journal-remote 2>&1 || :
getent passwd systemd-journal-remote >/dev/null 2>&1 || useradd -r -l -g systemd-journal-remote -d /%{_localstatedir}/log/journal/remote -s /sbin/nologin -c "Journal Remote" systemd-journal-remote >/dev/null 2>&1 || :
getent group systemd-journal-upload >/dev/null 2>&1 || groupadd -r systemd-journal-upload 2>&1 || :
getent passwd systemd-journal-upload >/dev/null 2>&1 || useradd -r -l -g systemd-journal-upload -d /%{_localstatedir}/log/journal/upload -s /sbin/nologin -c "Journal Upload" systemd-journal-upload >/dev/null 2>&1 || :

%post journal-gateway
%systemd_post systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_post systemd-journal-remote.socket systemd-journal-remote.service
%systemd_post systemd-journal-upload.service

%preun journal-gateway
%systemd_preun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_preun systemd-journal-remote.socket systemd-journal-remote.service
%systemd_preun systemd-journal-upload.service

%postun journal-gateway
%systemd_postun_with_restart systemd-journal-gatewayd.service
%systemd_postun_with_restart systemd-journal-remote.service
%systemd_postun_with_restart systemd-journal-upload.service

%files -f %{name}.lang
%doc %{_docdir}/systemd
%{!?_licensedir:%global license %%doc}
%license LICENSE.GPL2 LICENSE.LGPL2.1 LICENSE.MIT
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/crypttab
/etc/inittab
%dir %{_prefix}/lib/systemd
%{_prefix}/lib/systemd/system-generators
%{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/system-preset
%dir %{_prefix}/lib/systemd/user-preset
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/systemd/system-sleep
%dir %{_prefix}/lib/systemd/catalog
%dir %{_prefix}/lib/systemd/network
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysusers.d
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
%ghost %dir %{_localstatedir}/lib/systemd/coredump
%ghost %dir %{_localstatedir}/lib/systemd/backlight
%ghost %dir %{_localstatedir}/lib/systemd/rfkill
%ghost %{_localstatedir}/lib/systemd/random-seed
%ghost %{_localstatedir}/lib/systemd/clock
%ghost %{_localstatedir}/lib/systemd/catalog/database
%{_localstatedir}/log/README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.machine1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.resolve1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
%config(noreplace) %{_sysconfdir}/systemd/resolved.conf
%config(noreplace) %{_sysconfdir}/systemd/timesyncd.conf
%config(noreplace) %{_sysconfdir}/systemd/coredump.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
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
%{_bindir}/systemd-escape
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-machine-id-setup
%{_bindir}/loginctl
%{_bindir}/journalctl
%{_bindir}/machinectl
%{_bindir}/busctl
%{_bindir}/networkctl
%{_bindir}/coredumpctl
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-run
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-path
%{_bindir}/systemd-sysusers
%{_bindir}/systemd-firstboot
%{_bindir}/hostnamectl
%{_bindir}/localectl
%{_bindir}/timedatectl
%{_bindir}/bootctl
%{_bindir}/udevadm
%{_bindir}/kernel-install
%{_prefix}/lib/systemd/systemd
%exclude %{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%exclude %{_prefix}/lib/systemd/systemd-journal-gatewayd
%exclude %{_prefix}/lib/systemd/systemd-journal-remote
%{_prefix}/lib/systemd/systemd-*
%{_prefix}/lib/udev
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/var.conf
%{_prefix}/lib/tmpfiles.d/etc.conf
%{_prefix}/lib/sysctl.d/50-default.conf
%{_prefix}/lib/sysctl.d/50-coredump.conf
%{_prefix}/lib/sysusers.d/basic.conf
%{_prefix}/lib/sysusers.d/systemd.conf
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/90-systemd.preset
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
%exclude %{_mandir}/man8/systemd-journal-remote.*
%{_mandir}/man8/*
%{_datadir}/factory/etc/nsswitch.conf
%{_datadir}/factory/etc/pam.d/other
%{_datadir}/factory/etc/pam.d/system-auth
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.resolve1.service
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
%{_prefix}/lib/systemd/catalog/systemd.*.catalog
%{_prefix}/lib/systemd/network/99-default.link
%{_prefix}/lib/systemd/network/80-container-host0.network
%{_prefix}/lib/systemd/network/80-container-ve.network

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files libs
%{_libdir}/security/pam_systemd.so
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libnss_mymachines.so.2
%{_libdir}/libnss_resolve.so.2
%{_libdir}/libudev.so.*
%{_libdir}/libsystemd.so.*

%files compat-libs
%{_libdir}/libsystemd-daemon.so.*
%{_libdir}/libsystemd-login.so.*
%{_libdir}/libsystemd-journal.so.*
%{_libdir}/libsystemd-id128.so.*

%files devel
%dir %{_includedir}/systemd
%{_libdir}/libudev.so
%{_libdir}/libsystemd.so
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_libdir}/libsystemd-journal.so
%{_libdir}/libsystemd-id128.so
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/_sd-common.h
%{_includedir}/libudev.h
%{_libdir}/pkgconfig/libudev.pc
%{_libdir}/pkgconfig/libsystemd.pc
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc
%{_libdir}/pkgconfig/libsystemd-journal.pc
%{_libdir}/pkgconfig/libsystemd-id128.pc
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
%config(noreplace) %{_sysconfdir}/systemd/journal-remote.conf
%config(noreplace) %{_sysconfdir}/systemd/journal-upload.conf
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_prefix}/lib/systemd/systemd-journal-remote
%{_prefix}/lib/tmpfiles.d/systemd-remote.conf
%{_prefix}/lib/sysusers.d/systemd-remote.conf
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/systemd-journal-remote.*
%{_datadir}/systemd/gatewayd

%changelog
* Fri Oct 03 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 216-9
- Update to latest git, but without the readahead removal patch
  (#1114786, #1141137)

* Wed Oct 01 2014 Kay Sievers <kay@redhat.com> - 216-8
- revert "don't reset selinux context during CHANGE events"

* Wed Oct 01 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 216-7
- add temporary workaround for #1147910
- don't reset selinux context during CHANGE events

* Wed Sep 10 2014 Michal Schmidt <mschmidt@redhat.com> - 216-6
- Update timesyncd with patches to avoid hitting NTP pool too often.

* Tue Sep 09 2014 Michal Schmidt <mschmidt@redhat.com> - 216-5
- Use common CONFIGURE_OPTS for build2 and build3.
- Configure timesyncd with NTP servers from Fedora/RHEL vendor zone.

* Wed Sep 03 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 216-4
- Move config files for sd-j-remote/upload to sd-journal-gateway subpackage (#1136580)

* Thu Aug 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 216-3
- Drop no LTO build option for aarch64/s390 now it's fixed in binutils (RHBZ 1091611)

* Thu Aug 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 216-2
- Re-add patch to disable resolve.conf symlink (#1043119)

* Wed Aug 20 2014 Lennart Poettering <lpoetter@redhat.com> - 216-1
- New upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 215-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Dan Horák <dan[at]danny.cz> 215-11
- disable LTO also on s390(x)

* Sat Aug 09 2014 Harald Hoyer <harald@redhat.com> 215-10
- fixed PPC64LE

* Wed Aug  6 2014 Tom Callaway <spot@fedoraproject.org> - 215-9
- fix license handling

* Wed Jul 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 215-8
- Create systemd-journal-remote and systemd-journal-upload users (#1118907)

* Thu Jul 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 215-7
- Split out systemd-compat-libs subpackage

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 215-6
- Rebuilt for gobject-introspection 1.41.4

* Mon Jul 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 215-5
- Fix SELinux context of /etc/passwd-, /etc/group-, /etc/.updated (#1121806)
- Add missing BR so gnutls and elfutils are used

* Sat Jul 19 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 215-4
- Various man page updates
- Static device node logic is conditionalized on CAP_SYS_MODULES instead of CAP_MKNOD
  for better behaviour in containers
- Some small networkd link handling fixes
- vconsole-setup runs setfont before loadkeys (https://bugs.freedesktop.org/show_bug.cgi?id=80685)
- New systemd-escape tool
- XZ compression settings are tweaked to greatly improve journald performance
- "watch" is accepted as chassis type
- Various sysusers fixes, most importantly correct selinux labels
- systemd-timesyncd bug fix (https://bugs.freedesktop.org/show_bug.cgi?id=80932)
- Shell completion improvements
- New udev tag ID_SOFTWARE_RADIO can be used to instruct logind to allow user access
- XEN and s390 virtualization is properly detected

* Mon Jul 07 2014 Colin Walters <walters@redhat.com> - 215-3
- Add patch to disable resolve.conf symlink (#1043119)

* Sun Jul 06 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 215-2
- Move systemd-journal-remote to systemd-journal-gateway package (#1114688)
- Disable /etc/mtab handling temporarily (#1116158)

* Thu Jul 03 2014 Lennart Poettering <lpoetter@redhat.com> - 215-1
- New upstream release
- Enable coredump logic (which abrt would normally override)

* Sun Jun 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 214-5
- On aarch64 disable LTO as it still has issues on that arch

* Thu Jun 26 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 214-4
- Bugfixes (#996133, #1112908)

* Mon Jun 23 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 214-3
- Actually create input group (#1054549)

* Sun Jun 22 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 214-2
- Do not restart systemd-logind on upgrades (#1110697)
- Add some patches (#1081429, #1054549, #1108568, #928962)

* Wed Jun 11 2014 Lennart Poettering <lpoetter@redhat.com> - 214-1
- New upstream release
- Get rid of "floppy" group, since udev uses "disk" now
- Reenable LTO

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 213-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kay Sievers <kay@redhat.com> - 213-3
- fix systemd-timesync user creation

* Wed May 28 2014 Michal Sekletar <msekleta@redhat.com> - 213-2
- Create temporary files after installation (#1101983)
- Add sysstat-collect.timer, sysstat-summary.timer to preset policy (#1101621)

* Wed May 28 2014 Kay Sievers <kay@redhat.com> - 213-1
- New upstream release

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 212-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri May 23 2014 Adam Williamson <awilliam@redhat.com> - 212-5
- revert change from 212-4, causes boot fail on single CPU boxes (RHBZ 1095891)

* Wed May 07 2014 Kay Sievers <kay@redhat.com> - 212-4
- add netns udev workaround

* Wed May 07 2014 Michal Sekletar <msekleta@redhat.com> - 212-3
- enable uuidd.socket by default (#1095353)

* Sat Apr 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 212-2
- Disable building with -flto for the moment due to gcc 4.9 issues (RHBZ 1091611)

* Tue Mar 25 2014 Lennart Poettering <lpoetter@redhat.com> - 212-1
- New upstream release

* Mon Mar 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 211-2
- Explicitly define which upstream platforms support libseccomp

* Tue Mar 11 2014 Lennart Poettering <lpoetter@redhat.com> - 211-1
- New upstream release

* Mon Mar 10 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 210-8
- Fix logind unpriviledged reboot issue and a few other minor fixes
- Limit generator execution time
- Recognize buttonless joystick types

* Fri Mar 07 2014 Karsten Hopp <karsten@redhat.com> 210-7
- ppc64le needs link warnings disabled, too

* Fri Mar 07 2014 Karsten Hopp <karsten@redhat.com> 210-6
- move ifarch ppc64le to correct place (libseccomp req)

* Fri Mar 07 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 210-5
- Bugfixes: #1047568, #1047039, #1071128, #1073402
- Bash completions for more systemd tools
- Bluetooth database update
- Manpage fixes

* Thu Mar 06 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 210-4
- Apply work-around for ppc64le too (#1073647).

* Sat Mar 01 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 210-3
- Backport a few patches, add completion for systemd-nspawn.

* Fri Feb 28 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 210-3
- Apply work-arounds for ppc/ppc64 for bugs 1071278 and 1071284

* Mon Feb 24 2014 Lennart Poettering <lpoetter@redhat.com> - 210-2
- Check more services against preset list and enable by default

* Mon Feb 24 2014 Lennart Poettering <lpoetter@redhat.com> - 210-1
- new upstream release

* Sun Feb 23 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 209-2.gitf01de96
- Enable dnssec-triggerd.service by default (#1060754)

* Sun Feb 23 2014 Kay Sievers <kay@redhat.com> - 209-2.gitf01de96
- git snapshot to sort out ARM build issues

* Thu Feb 20 2014 Lennart Poettering <lpoetter@redhat.com> - 209-1
- new upstream release

* Tue Feb 18 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-15
- Make gpsd lazily activated (#1066421)

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
- Flip journalctl to --full by default (#984758)

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-9
- Apply two patches for #1026860

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-8
- Bump release to stay ahead of f20

* Tue Dec 03 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-7
- Backport patches (#1023041, #1036845, #1006386?)
- HWDB update
- Some small new features: nspawn --drop-capability=, running PID 1 under
  valgrind, "yearly" and "annually" in calendar specifications
- Some small documentation and logging updates

* Tue Nov 19 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 208-6
- Bump release to stay ahead of f20

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
