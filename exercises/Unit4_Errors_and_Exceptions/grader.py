"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'4.2.1': 'eNqFUctOwzAQvOcrVj45khX1dSrqBYgEqgSiiFMTVaG2iWniWFm3oX/POmkLFQd8Wo09szNjU7um9dCgAK9qp02lokgqDdtNbRCN/eAW43kEdDQswOKaYaHVpmoKyfIeLxAVaWjeYOIKXyafjbH8LJfUOxlmHgtgtnEq2eKBxTEsFrDOBWS9RjisgNNOCESo9+jhaFQlobBAEv4IlUHPzg5xZ9z/9iThf83cgCP8yrEkg/Xgrid2xpdAhi13dNOxmJKCLucXw7pMutZ4xdmXOGZ2LCaZvV09L9OnzE7FLLMnoUtBbkjNx8lIwCQZUSV8GuYZzXlYX1S6aWslKahVOFTwriAkdUpS8lX68va4Su/J/HXUu4f0bvka4H4nZ63y+9bir+KgK5UdujV47pqJn7+OxYkb9tGLazcCdkoRfCgqI4FT5rgnh8fEzKNvMImygw==', '4.2.2': 'eNptkEFLAzEQhe/5FY+cNpBCK3hR9tQuKJ6seFGLxN3ZGmwnyySt1l9vkl4UnEvgzZv3zWSgEf3r4I8NR3OlkGtEC47POrqRSkdvquxiJEkYm8Xc4sKgbXFZG+GQ8kTWLebmt9VHzzE57qnJHouYxMDxAP1EElb+mA2BO5EgGp5RTS81oZQOjIz3A83eTrPvPGIhlA7CcCXL8xbs9uVJ7wT66mlKORDpNJFWat3dP96uu1Ve7s8xy5tuefdQ1IpqNAfZu11llYXwGeQjXqMQz2KQDJ6CpPgfyZ4/0Fi1UT8FkWi8', '4.3.1': 'eNp9kkFPwzAMhe/9FVZOLaoQ7Dgol9EJhEBiiBNMU0nNFqlNRuzC9u9x23XrgNJLlMT+3utzcnwHvciIzNKGlqJxAPK1e0jA0otqN2p+AelG784e3H3GemXsclpZzcbZ1Hvn1bxrR887Srh2xvIix8/k/PQshjLbLNhnxnZHESQJqLLmYa5ieG0Y9afkFi4TkOWEPjyHowjIgWGglauKHJom1dSz3473jb+UR38r9xtqx9OsIIxBSTlcDcsKg7CVxY3GNdfJyCIxCAlw/JNryFjizGoMBS/FkYiUFXGLgq2rPAxlGgR5MySq3nQhwKMxtfTe1T+ziQ82o6OYeYWgxY0rAetSaKx10EOXWJmlj8+3s/Ra3sGwkvxc92iCyU06uXuqyxu9UAa9JvgyLG3QpcuuQF/HA5ndxUvwhlsnO8PC655oFO8oA9J709i3HffSE8I8+AZIWPJ/'}


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
