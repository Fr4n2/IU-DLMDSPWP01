"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'5.4.1': 'eNqFUsFKAzEQve9XjDllcbuoKFKxp7WgCIItnmpZ0mzaBjbJkkmF/r2TdG1LrRhyyeS9NzNvRpvO+QAYRNAYtMQsa9QSZN04yS3mDxnQqWAEFmdsuoexefoQiIrovCrryKhrcB4Yy0sMXnc8h4sRPQtgYa1AtgQHq1SDIIDgEWRXLCktiWhAW5gxo4SNHAwNm+8KiMeosKY6VoqKCJ5XBZgC3pxV+R7Sl5OQmlK5kACkZTQi5UpfrgEGl2BOaTx+/tOIISKj55kueuOkaI+cwzPO8dlNAbc/9y7d+wKG8/zYU7FAjmX0gtIN4K68yuERrtVgGNuhcOxQW+m8VzKw31SyLzEPsy07iqmvv/MfMnzuzYljAFy7TdvAQkEcZOe6TUuizkZx2wjfAOnqFCIjJuP3j5fJ+Il6P9mZ6nlcvU5jPOlzttsJ0ugngyCF91sanR0o04XtwWEk+9Ne5kVPTi5EbixROtNtAm3ZzpB2m+BxGoSfZ98iV9tu', '5.4.2': 'eNptUl1LwzAUfe+vuOYpgRkmiqDQvWwTRRCd+iSjxPZmK2xJTVIRxP/uTdrVDsxLuOeec3I/Uu8b6wJUtgzoQ5ZVqKEs+pAbL64zoKMhB+PfmP9olUO2TiCxCNayiPyiAOuAsZRR3mPnKn1wdcMFnOSUnAALWwTdmjLU1oBBrDyoSIw8szmSs9lsxqA2Md0rByLsWx+gtCYoIqhDA4Bfat/sEDhpQUopOsdGObKkanueXNjyhe7HhHORSMkg77lyg2GYQyrg+9D9NegfqqePJvBgDU5g2pm41pj/XlolnH+ie7ce8xu18zhWSLp4FIjxCPqcVvWudeghz2H6N4pxx9yLbiYNSY/GqPm5iMIrUKai6PQihWeXQw+d0GFonYHo3cNWQx08baBpA8uy1fLp9W61XFBzo58wv13O758jlh7lbNjuVvnRZsJWdcVRG7GQ2tP6nMMy0AiHLycm2Tr7BbEF0gE='}


def _load(eid):
    src = _zl.decompress(_b64.b64decode(_BLOBS[eid])).decode("utf-8")
    mod = _ty.ModuleType("grader_" + eid.replace(".", "_"))
    exec(compile(src, "<grader:" + eid + ">", "exec"), mod.__dict__)
    return mod


class Grader:
    """Runs the hidden checks for a single exercise and prints feedback."""

    @staticmethod
    def run(eid, namespace):
        bar = "=" * 64
        if eid not in _BLOBS:
            print("No grader is available for exercise", eid)
            return
        mod = _load(eid)
        required = getattr(mod, "REQUIRED", [])
        missing = [n for n in required
                   if n not in namespace or namespace[n] is None]
        print(bar)
        print("Grading exercise " + eid)
        print(bar)
        if missing:
            print("Could not find: " + ", ".join(missing))
            print("Keep the names exactly as given in the task description.")
            return
        checks = mod.CHECKS
        passed = 0
        for desc, fn in checks:
            try:
                fn(namespace)
                print("[PASS] " + desc)
                passed += 1
            except AssertionError as e:
                msg = str(e)
                print("[FAIL] " + desc + ((" -> " + msg) if msg else ""))
            except NotImplementedError:
                print("[FAIL] " + desc + " -> not implemented yet")
            except Exception as e:
                print("[ERROR] " + desc + " -> "
                      + type(e).__name__ + ": " + str(e))
        print("-" * 64)
        print("Result: " + str(passed) + "/" + str(len(checks))
              + " checks passed.")
        print("All requirements met. Well done."
              if passed == len(checks)
              else "Keep going - review the failed checks above.")
        return passed, len(checks)
