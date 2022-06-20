from rest_framework.exceptions import ValidationError


BADWORDS = ("meapilas", "aparcabicis", "caraanchoa", "bobo", "cabrón", "cabron", "idiota")


def badwords(description):
    """
    Valida que la descripcion no contenga ninguna palabrota
    :return:
    """
    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("La palabra {0} no está permitida".format(badword))
    return True