import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Schoolkid
from datacenter.models import Lesson
from datacenter.models import Commendation


def create_commendation(name, subject):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist:
        return "Такого имени не существует"
    except MultipleObjectsReturned:
        return "Найдено несколько человек с таким именем, уточните запрос"

    lessons = Lesson.objects.filter(year_of_study=child.year_of_study,
                                    group_letter=child.group_letter,
                                    subject__title=subject).order_by('-date')
    lesson = lessons[0]
    compliments = ["Молодец!", " Отличнос!", "Великолепно!","Заебись"]
    compliment = random.choice(compliments)
    Commendation.objects.create(text=compliment,
                                created=lesson.date,
                                schoolkid=child,
                                subject=lesson.subject,
                                teacher=lesson.teacher)


def fix_marks(child):
    Mark.objects.filter(schoolkid=child,
                        points__lt=4).update(points=5)


def remove_chastisements(child):
    Chastisement.objects.filter(schoolkid=child).delete()


