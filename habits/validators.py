from django.core.exceptions import ValidationError


class HabitValidator:
    def validate_reward(self, attrs):
        if attrs.get("reward") and attrs.get("related_habit"):
            raise ValidationError("Нельзя указать вознаграждение и связанную привычку вместе.")

    def validate_time_needed(self, attrs):
        if attrs["duration"] > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")

    def validate_related_habit(self, attrs):
        if attrs.get("related_habit"):
            if not attrs.get("related_habit").is_pleasant:
                raise ValidationError("Связанная привычка должна быть приятной.")

    def validate_pleasant_habit(self, attrs):
        if attrs.get("is_pleasant"):
            if attrs.get("reward"):
                raise ValidationError("У приятной привычки не может быть вознаграждения.")
            if attrs.get("related_habit"):
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки."
                )

    def validate_frequency_habit(self, attrs):
        if attrs.get("frequency") > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

    def __call__(self, attrs):
        self.validate_reward(attrs)
        self.validate_time_needed(attrs)
        self.validate_related_habit(attrs)
        self.validate_pleasant_habit(attrs)
        self.validate_pleasant_habit(attrs)
        self.validate_frequency_habit(attrs)
