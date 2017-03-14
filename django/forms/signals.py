from django.dispatch import Signal


post_init = Signal(providing_args=["form"])

post_clean = Signal(providing_args=["form", "cleaned_data"])

post_save = Signal(providing_args=["form"])
