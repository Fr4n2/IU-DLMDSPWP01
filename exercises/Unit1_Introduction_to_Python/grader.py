"""Autograder for this unit. The grading details are intentionally
encoded so you cannot read the expected results directly. Run an exercise
template to get pass/fail feedback per requirement."""
import base64 as _b64, zlib as _zl, types as _ty

_BLOBS = {'1.1.2': 'eNqVU8FO4zAQvecrRj4lUoUouSH1BEUgDmhZVkKKospxpjTCdSqPC8vf73icZgNbVpDk4Hjee37zJmlxDWa11c+YOyrOM+CrgQU4qlTcXTW99q2q80JKmgh9gI46R0E7g3kzA9tRKEC7Fiy6vClgsYByBkqosN1TgAZBCw76NZTg+1dSU0FtbT4R9R9FfRKFde/BQ+egKfgA1GYTtcAhtsRlg9b+K2wiV/H9ly1LE5c+CjEqcZNbdhGpxJ7Z05NFoJ02qLKslbgIw5fSituMXUVp3uSoTuVRj+ozwHwGZwy4U+/ybqrTmh/p41FJKk01r6uztHWnmHLQSS3sLBuGrfbPoANUHFJdmd7WYw/rPSfzjZHHakdCi04L/gbgSlvCGJ8D3O7CG6SJc8X1AQQqEmPuXrsnzMvh0EOJfR0vHo+IPw5mTFL8j8MHvxeDg7PXLmzYWxonRUAymd0vf/y6uV9ecgzvQpjkGtejfHZxvby4/RnhYiGfkMB41IHlx1jK3yUc9NLPVswG2jg1GRjJxIj78x5NsG9CYMyIHxxAi4EBNBzwQifSSTqFhBXfmVZnfwDv/yyq', '1.1.3': 'eNqNkt9PgzAQx9/5Ky480YiLbNmLZk9zicYnZ3wihCAcS+Noa1vQ/ffeUTaz6YMNgXJ3n/vxbWVntPVgK9XoLooabKEu3yon60Q5cRsBrRZWoFwe90p+9Fi+I5pS2wZtXIz+yjmkHG2SFwJWK8iLFGLsjD+AVKb30PXOw04OCMGqe0/m+AKOD1lM4GE+vsN+MVmmxOchi1/1sxT4maKz4jhQGO//E7XaQknNsy47TObLieNF4iDhecg5449UPrlJYSkuwWwpihPoEFUK+GWIdugTkZJSJy+TA5Oc/6caL9mSR2nPXk5y7j2mnlVNkwzijivMKmNQ8e8p9CTSXjqfcBExqkTRpOWn1WoHFl2/92Mr4eBiuCKjsSE+irab59fH7eae5/9TvPXDZv30wu6xcBJb7PSADpre7GVdedrqcUZZQ01JHZ3kdOFEOjGG+kDLVCut89c8HYwVmA26hwYDHSyEF9E30dXSlw==', '1.2.1': 'eNqdU0FP2zAYvedXfMrJBjdqMxVt03ZinUCcBtouJYrc9EsXLbUz2wHKr+dzbNKOVQjhS6z4vef3nu1m22njwEi11tskWWMNpcGa7ZyAXcc/J0DDoOuNAttvGZMwgRWHkxPIodYGpIAVNAoem+6ZxINOVf5R+l4xZaNMDV9B2WVKOqX920uD6xKN0SYthnVpLZIXubKsZsuZgFzAh0LAOOUcvsAMJ5+OwKcCphE7KziZzF8BzzKC51kgZHM/nw+kaTYfaTFEqObtKXwppW+EiBtk+Tzy/FDEDXqZ/zTKMfL7kY+AnSPEMkJ61ZDYlk3IINl6Iax4sad176L9U0rbWEcnyAWEGZ0jFXJ4GWIzZwJuRwk/0nuj1QbuZNtjuBMxJO3a9Q50DS2qjfsNKZyCdYZM7NttLNq3t+vMbl9nvCXDKRb8ZazvsrUoIMWHDiuHa7L1y1tceLnBZ6+Qtmgn0d3g1qaDDj5U2LkDwn7XjvST5Hrx4+fl9eKbL/6o2/OLxfnVjV8emCyttDFkBLSC4WFAJSl6Kp4fChf/Aw97DNDwZ8SG/g6DEet4LjHWTewieQLfeSk3', '1.3.1': 'eNqFUkFOwzAQvPcVK59scBEUyqFST1AJxAkqTiWqHMcBq7UTxW5pQP07aztNKReiSFHGOzO7s9amrhoPjbBFZQaDQpWwdE5RwSFnkwHg0yi/aSy4jaF0B0NoGZydwQjKqoEdhxa0hS9dJwpLGnKZC6clta4TKWEK1i1IrpxfltqTLMItwosrDiMO1xxuEiixGYcH30SQyckxB5IH6JJD9wZInlSNs31UETgGTlbSlkOhpadRljGYTgGFj04XdVVTRNj/NEkO46XA/p0vZLQMAWH9u6JX4648PBYpSeYifLT1FNu/ZX1BDKer2FiNWoYOseSa/dW1LOtZfXr7HgrVVhgVCETksiDHLnrKIlRkwXIL5/DXFrMdJdttUGmPfmpXI8lom5LisFLtdC1MXghYTdJtwiyTxypjx/n6qNfaedoyDt9IiD/b5LXiyS7tSXtlHGX7uAu05fB2MgYpdAG28ocb6z9U6EubjRnO57OoogvhFW7xZfb8+vgyuw/z/l7a3cPs7mke0ChNSdJyUawXgE/tPyLkjFivkQ5oQPjh3jPesWXVNEp6qGyX6C8Np7yLlHSCnGzwAx6/AWY=', '1.4.1': 'eNpdUkFugzAQvPOKlU9GshBEOVXKKY3Uqqcmai8hikwwwg3YFmtC8vsudhq15YDGnp3ZnQXdOzt4sCjAq941ulNJUqsGTsdByZobTJ8SoKeBFRjcs/n2eL0dT3hhh8DUxPxos/5cz5ingXJEWcyc9G32ZbXhtQB2vWWzOFZM2rdgnTLcETWxFCRC08aeoW+bTYP2irOruJUmF3lpClGUZiGWpbm7DHZCatVwF88SUVGqeL2CPc+zXAC9UgG8mHER8WLGS8IHAeWjJ+tHJLXy42Du4qAN0qAMwqALCezowbcKWlqOGtjvGWTXcY3aoJfmpLgU0HRWesppavhFVA+isQNQWQXahATpn9EqSwu7yG5UOBcoeWrBj65TEIauVLRBliTbzfvH63bzTJv5/93WL5v1224mgjMPNAKtGNa7TzL2NvpEbwQeowGetXOqTpm4/yGpSA7JN9m4qFk='}


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
