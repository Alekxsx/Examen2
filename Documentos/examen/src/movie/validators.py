from django.core.exceptions import ValidationError

def validate_studio(value):
    if "-" in value:
        return value
    else:
        raise ValidationError("Inserta un guion para el estudio")
