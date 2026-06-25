"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'3.1.1': 'eNplT7EKwjAU3PsVR6YEslhxETLVguJkxamUksYUhTYpSQr9fNOIDvqGx3Hv7rh31z1UG+xEjWf7DHF6CBhfk0i2g+z04EmTDtJ77QJ6WhNJOEi3roTUF3Wk4TAiZxACNU3klnHQpM7ZX9LyNuw+hiXKNlGWVeXldqrKQ2zz06U4lsX5uvIpjBKnw+yMR3hoGIzWByg7jtaAJhNXdjaBYZJP52N+epjxrMleQk9E/w==', '3.2.1': 'eNp1kUtPwzAQhO/5FaOc7OJWTZGQeJ1KJBAnWnEqUeUkThvRrCPbadV/j+PSBwL2YnvknflWWzetNg7UNe0e0oJaASOp1E0UlapCsaSWkeV3EXxVeATZRWyt8nqcBVH6l7eQuWXVRkvHKrZIBCYC15nA6co5xwMSNbz9r4vakTRG7tliLDDOuMBZ8S5JsBhi8sOn0gZL1NRTrxRLJt+ofZHHPQwz6o+aHPMoyZiffsh+oHZ08YkRv0f+l3xu+o0uBfIAdxB8r+0axqRXco7BwEMfx78R+DhZ9RXvjKYVtnLTKWjyTIdchNGhK2wUrdwaMa5gnelRoln69v4yS5886MU6ps/p9HXeayGBxVtVOG1qq0rM5yka6Yq1sjCqUkZREfI+Se98KpXH3JraztlYhOVzEWXRF48RnOU=', '3.2.3': 'eNplksFq3DAQhu9+ikEnCRyRTU9Nu6fNhpZCoAntZTFhYsnYiTQSHjmNKX33jr1saBPhg2ZG8+n/Rx5iTmOBjOSQQb7saqAp5nkJKNeQuIbiY+6G4KvK+Q7a+zZ4JE1sLiuQ1cEWiA8qJHTHmmrWgpPCqdfGJ7fstfkEWfKJbcbS28c0kJZLVbEtPyuzNmZnr7Dg9YjR69/qRV3C4byGTQ0XjRydl3hzbiVF2RJSDR8kav4YW9K9YLQIH8j5l+01BvZHqFt0djofI2T24rxHxlJG7TrhtilMkVgZ2ceJC4y+TCMBngb0Kkr9yxioSP9BZDV2YEJtLE9RGwPbLYhGRQlu8AYizkKMOJC0wPEymP9D4QPrTua4AG1I7WGz2m0MnMGFWDTwGTb+7KNkZagBnjFMHrhPU3Dw4KH0/gSOyztU1e3++4+vt/sr8f7mhXZf9rtvd0t+VaDXKsPu7ieIW1j4vOoWsTP8Gkr/Dl+ffgZTV031Fwt+sr8=', '3.3.1': 'eNptULFqwzAU3PUVhyaplUONSYfQTqmhpVNTOpUQFPu5NjiykBQaL/32yjI0CfSNd/fu3r3uYAcXYI4HO0J7GMtYTQ2qXdMFYbxcMcRp8AjjP3kEd31niG8TfJpgu9BOmy8S+Z1cOPKttiSyXCGXSTRGUYGbayFusUys7wdLCp0J5CqyIYobcVIY52XtPcX79N6Lph90EEkvkaGQeEBO2b0CTyB8Oxz7GnvCT8H/3/6LmRyWFw7n/AuXJWdsU759vGzKp3jXVf31c7l+fZ/QlCQmzkNjovHdhRbV4BxVYW4IbepzSa7mB0vFtuwX9w5y+A==', '3.5.1': 'eNplUsFu1DAQvecrRj45EGUBcVq0h2qbiooi1F04raKVN5503Tq2sadqV4h/Z5xsCaiWD07e+L15z2OG4CNBUE6rBLyDrsCnCgiH0BuLRaGxh26vD9KlclkAL4qn6ZBXH/0A6adVtjvicAIzMXYRFeEe3Z1xOBbjc4eB4HrEmxh9nEmiMgnhIiWMZLwbUSmMS6Sshe3tzcWZvTcx0RKCCfCCztqiHAl7WIFLO6H7Pfk9w4ZQtCOkGXpxVg8POp9l+Qkeo2VETLXLxWIh4C3HUAdFx/reGyc5FkG1Ppw1dBYJur5UpK6iGlD+Es9iCbt3Fbyv4EPL5af5+2P7+9yb1H1mYsPOuDtRZekJOqjuYSLl6HTuW4ptc9Osv8MbuNp8+wr/3PovXpk5JhI1RgjWJJKZcMddtCWsVnMnWV4dLELnHaGjBMNjIhgUdUegI8JfT6IoNs3tj+tNc8mNvQp0/blZf9lmZJSW4ikywFM0MwD5/Hr8G3jCIBtLk1GjWdp0ykL0Tyk74hErq6It/gAuAMwb'}


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
