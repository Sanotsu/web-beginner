from examples.demos import demo_weight_trend
from examples.demos import demo_weight_intake_exercise_detail
from examples.demos import demo_weight_intake_simple
from examples.demos import demo_weight_intake_exercise_simple
from examples.demos import demo_weight_intake_exercise_simple_optional
from examples.demos import demo_weight_intake_exercise_separated


if __name__ == "__main__":
    demo_weight_trend()
    demo_weight_intake_exercise_detail()
    demo_weight_intake_simple()
    demo_weight_intake_exercise_simple()
    demo_weight_intake_exercise_simple_optional(
        is_show_intake=True, is_show_exercise=True,
    )
    demo_weight_intake_exercise_separated()
