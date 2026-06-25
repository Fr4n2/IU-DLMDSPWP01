# Entity Hierarchy with super()

**Difficulty:** Medium  
**Course unit:** Unit 2.2 - Classes and Inheritance  
**Context:** Game development

## Background

Inheritance shines in game entities. A base `Entity` holds shared state (name, hp); subclasses add their own behaviour and reuse the parent via `super().__init__(...)`.

## Task

Implement `Entity(name, hp)` with `is_alive()` returning `hp > 0`. `Player(Entity)` calls `super().__init__` and adds an empty `inventory` list. `Enemy(Entity)` adds a `damage` attribute and a method `attack(self, target)` that reduces `target.hp` by `self.damage`.

## Requirements (graded)

- Entities start alive
- `attack` reduces hp and a target dies at hp <= 0
- `Player` has an empty inventory; both subclasses inherit `Entity`

## Running the test

From inside this unit folder, run:

```bash
python ex_2_2_2_entities.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
