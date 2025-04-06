from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def rating_to_stars(rating=0):
    full_star = '<i class="fa-solid fa-star"></i>'
    half_star = '<i class="fa-solid fa-star-half-stroke"></i>'
    empty_star = '<i class="far fa-star"></i>'

    rating = round(rating * 2) / 2  # Round to nearest half
    full_stars_count = int(rating)  # Number of full stars
    half_star_count = 1 if rating - full_stars_count >= 0.5 else 0
    empty_stars_count = 5 - full_stars_count - half_star_count

    return mark_safe(
        full_star * full_stars_count +
        half_star * half_star_count +
        empty_star * empty_stars_count
    )