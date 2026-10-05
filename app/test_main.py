import pytest
from typing import Any


from app.main import get_human_age


class TestGetAgeInHumanYears:
    def test_should_return_list_of_two_int(self) -> None:
        result = get_human_age(14, 17)
        assert (
            isinstance(result, list)
            and len(result) == 2
            and isinstance(result[0], int)
            and isinstance(result[1], int)
            and result[0] >= 0
            and result[1] >= 0
        ), "Function should return list of two non-negative integers"

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Cat and dog - zero human years"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Cat and dog - zero human years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Cat and dog - 1 human year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Cat and dog - 1 human agyeare"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Cat and dog - 2 human years"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Cat and dog - 2 human years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Cat - 3 human years, dog - 2"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Cat - 3 human years, dog - 3"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Cat - 21 human years, dog - 17"
            ),
            pytest.param(
                15,
                24,
                [1, 2],
                id="Totally different ages"
            ),
            pytest.param(
                10_000,
                10_000,
                [2496, 1997],
                id="very large ages"
            ),
        ]
    )
    def test_should_convert_to_human_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestErrorRaise:
    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param("2", 3, id="cat_age is string"),
            pytest.param(2, "3", id="dog_age is string"),
            pytest.param(None, 3, id="cat_age is None"),
            pytest.param(2, None, id="dog_age is None")
        ]
    )
    def test_should_raise_type_error_for_non_int_args(
        self,
        cat_age: Any,
        dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    def test_should_raise_type_error_for_float_args(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(2.5, 5.73)

    def test_should_raise_value_error_for_negative_args(self) -> None:
        with pytest.raises(ValueError):
            get_human_age(-3, -13)
