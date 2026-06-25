"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'6.2.2': 'eNp1U8FuEzEQve9XPPnStdiuhMSpopVQGkGFCqKlpxBV7nqSmOx6ke0lIPHxzNihaSIxB6/HnnnznmfW0grdYzfYWPuoLyqwiYdL+LhQ72++Ps4+396++3R9r5b51sRIIcFF52MyvqNa4hv0LiYN4y168vlM4+oSbxp8y3liR3gYppjwRDA5FzuXNjCJ0w17XT96amCsbdCNw+BSgx9T3KiXJEzf1y+JNIgpaKzGgA7OZyW6gaKfFH6DfOL1UFVghS/nOL8uwP24Y+mLruUNhfoEq7zA99F5shym8AeqFbfmcJ0vJX67k4SFyhoU12cV8ik6ZJeVLC+eH2avp1Zrlxj2FUNowSilOGFwkXWumfXZIYQXdfZPhqoymuWGOvur3uoDunByTZFBfhoomESZ8iFGzK2wzVKPj8UCpSl4uOrk4Pz10VBw4b1qjbd7t4h+9rN0fTQVY7AUEDfj1FtpTUbA+RXatpVPgZBdmYDqbv7l4eZufi2tOp3R2Yf57OO93OQCQsAnwzPy35ESyQaRfHRPPSGz4SaV30I31bL6C01o6dU='}


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
