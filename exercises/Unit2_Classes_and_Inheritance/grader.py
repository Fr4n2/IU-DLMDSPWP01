"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'2.1.1': 'eNptUE1Lw0AQvedXPPaUQA5N9CTkVAOKJyuepMh0M7Uh2U3Zmfj73SQtqegeFh5v3sdMw0fYTzuMXjmkXrKHBPG5DhW8fBhHHV9ps585GynXpdkMSISDwqYZqgoFyDdXUN6CuxyGyZ5gqe/hRlG03gZ27BXHMDhszOJeLvaiFLQqNr9jyktOEe3mCZwpkOPYbjEVVuiJcSBh80/D+0nIk0gZl71kkR44Vmr4zPHzapJkV7++P+/qx1jozyG2T/X25W1i5pDU3EjXzVr/tYZ8twTbDzIGNvl69CxP9skPHxZ3Vw==', '2.2.1': 'eNqlk8tOwzAQRff5ipFXMXIQaReIiq7aIipWvFYQRW7iUEuOU/mB1L9n7IRWgZYNXlnJzJ1zbya1aKAqldCptnSWAB4Hc9D2jbwYLrXUH0vuOCnStysGOYNJweBwpbGBWyuMgyDiKMznMGVAyiBaltB668AI540GtxWgfbsRBroGdp3UzpIkqSMDivyDQQ4N61pwded15WSnT3ZM8ap5K+Zkf01GBvjGpu4ycEgKGeQUbiEX2Q266bTaR3zF0U4kh1o2jTB2Bukkm9KLiwki5Ac7Um+Fke5o6TxhZDtLJa3U1nFdIRaLCiGMZ+FIQZFsJNenPYyGxnQtfBefkTwZcg9Ef097jyrhjJr+GjvEYcTO/D+L8ADnQFSTv+2XcQ5und12XtVYWilfC5DORkXEeVo9vq6fVkskOHpjYz/kpzApksX9avHwHLoiUHpY8H63bdyOfjGqzuugGf8ryoZ6dIBv2h03wsI+++TK46XqjBGVU/tYjzXHer+pVPBtTyfLjkt26BmnEbL4jqDnixmw4XNgV5F8ATXfOT0=', '2.2.2': 'eNq1U8FOg0AUvPMVL3uChDRUL8aKl4rWeNEaTw0xW3iWTWFL9m1r+HsXdgsV7cGDHHdn5s2bWXL8gOydl+KAvqTg2gPz1RCDpBV7LnmDiqU+W6DasRAuo6ADoAMkEqumvX/YrUshDWIahZDzim8wnl5YMCdCpaGeCHKDAuAyBzw5CIGh1EILJPgUuoCivo2AK4QOwDwvt0a15tn2v5zixOnXI+eFmRPD9MrYtAio9qRBYb7PEDRXG9TGMqwbJ8nGerPz4iexCIJ7XhKaOUV9E0dQIZcEcqdHOQh5+EMIwyh5MDHvVNOus0rNGMux65BZRNv4uQSsat1Az2CnSoKENGiZoV+HLl/Tngk4GGkKWaASGtz9GZHvDbXlDN0EPwd00N/1vWXy8va4TO5MJj2p98SOZJZ680Uyf3ptYZ0pf3iANgcbeHj8O4LQwdwDsN1T23r7mLeiLAm4hshSOlDPcYkUnIZAZ0D7dVa2YdB4jdBWbPip9wW08h8o', '2.3.1': 'eNpV0E1LAzEQBuB7fsVLTgkE6cdN6KmWKp6selqWErvTNZAmJZO1XX+92a1FGwiEYfLMhzscY8rI/ZEYlrHNQjS0x27bUlCB9b1AOS0WCFxJlyltUzyxrFU1NZgZzGuDajop73Lnk1qPHywzFdexC5xt2JFqTcHv1hQo2RzTW6moDf5EHDrO+CBYtNckqI4JvSPfaPnfDXTOqtVYLKBKG9PJQO1dKsKYTQ2+rO8I/Bk73wzsb94N4x1fmUrNhhGKo+bDHLqMJRMdrAsutBeNr9w+eh9PcAExNZSkEJvVy/vTZvVQ9nSzJbF8XC2fX4fwWFjJsT+GOpteI3dHX1hvv53vpbmsXRtRix8OGnvf'}


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
