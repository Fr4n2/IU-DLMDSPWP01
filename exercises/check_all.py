#!/usr/bin/env python3
"""Run every exercise template through its grader and print a progress summary.
Unsolved templates simply show as not-yet-passing - that is expected."""
import os, sys, importlib.util, io, contextlib, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def load_module(path, unit_dir):
    sys.path.insert(0, unit_dir)
    spec = importlib.util.spec_from_file_location("ex_mod", path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    finally:
        if unit_dir in sys.path:
            sys.path.remove(unit_dir)
    return mod

total_pass = total_checks = 0
for unit in sorted(os.listdir(ROOT)):
    udir = os.path.join(ROOT, unit)
    if not os.path.isdir(udir) or not unit.startswith("Unit"):
        continue
    print("\n" + unit)
    for f in sorted(os.listdir(udir)):
        if not (f.startswith("ex_") and f.endswith(".py")):
            continue
        path = os.path.join(udir, f)
        eid = re.match(r"ex_(\d+_\d+_\d+)_", f)
        eid = eid.group(1).replace("_", ".") if eid else "?"
        try:
            mod = load_module(path, udir)
            from importlib import import_module
            sys.path.insert(0, udir)
            grader = import_module("grader"); sys.path.remove(udir)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                res = grader.Grader.run(eid, vars(mod))
            sys.modules.pop("grader", None)
            p, t = res if res else (0, 1)
        except Exception as e:
            p, t = 0, 1
        total_pass += p; total_checks += t
        status = "OK " if p == t and t > 0 else "   "
        print("  [%s] %-8s %d/%d  (%s)" % (status, eid, p, t, f))
print("\n" + "=" * 50)
print("Overall: %d/%d checks passing." % (total_pass, total_checks))
