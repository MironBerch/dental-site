from django.db.models import Q
from django.urls import reverse

from works.models import Work
from clinic.models import License
from staff.models import Staff
from services.models import ServiceGroup, Service


def get_search_results(query: str):
    query = query.upper()

    SITES = {
        'контакты': reverse('contacts'),
        'отзывы клиентов': reverse('reviews'),
        'лицензии и сертификаты': reverse('licenses'),
        'реквизиты': reverse('requisites'),
        'услуги': reverse('services_groups'),
        'цены': reverse('prices'),
        'персонал специалисты сотрудники': reverse('staff_list'),
        'клиника': reverse('company'),
        'галерея наши работы': reverse('gallery'),
        'карта сайта': reverse('site_map'),
    }

    results = []

    # Staff results
    staff_results = Staff.objects.filter(published=True).filter(
        Q(fio__iregex=query) | Q(information__iregex=query)
    ).values('id', 'fio', 'information')

    for staff in staff_results:
        match_count = (staff['fio'].lower().count(query.lower()) +
                       staff['information'].lower().count(query.lower()))
        results.append({'type': 'staff', 'match_count': match_count, 'data': staff})

    # Service Groups results
    service_group_results = ServiceGroup.objects.filter(
        Q(name__iregex=query) | Q(description__iregex=query)
    ).values('id', 'name', 'description')

    for group in service_group_results:
        match_count = (group['name'].lower().count(query.lower()) +
                       group['description'].lower().count(query.lower()))
        results.append({'type': 'service_group', 'match_count': match_count, 'data': group})

    # Services results
    service_results = Service.objects.filter(published=True).filter(
        Q(name__iregex=query) |
        Q(information__iregex=query) |
        Q(short_information__iregex=query)
    ).values('id', 'name', 'information', 'short_information')

    for service in service_results:
        match_count = (service['name'].lower().count(query.lower()) +
                       service['information'].lower().count(query.lower()) +
                       service['short_information'].lower().count(query.lower()))
        results.append({'type': 'service', 'match_count': match_count, 'data': service})

    # Works results
    work_results = Work.objects.filter(published=True).filter(
        Q(name__iregex=query) | Q(information__iregex=query)
    ).values('id', 'name', 'information')

    for work in work_results:
        match_count = (work['name'].lower().count(query.lower()) +
                       work['information'].lower().count(query.lower()))
        results.append({'type': 'work', 'match_count': match_count, 'data': work})

    # Licenses results
    license_results = License.objects.filter(published=True).filter(
        name__iregex=query
    ).values('id', 'name')

    for license in license_results:
        match_count = license['name'].lower().count(query.lower())
        results.append({'type': 'license', 'match_count': match_count, 'data': license})

    # Check for Pages
    for page, url in SITES.items():
        if page in query.lower():
            results.append({'type': 'page', 'match_count': 1, 'data': {'title': page, 'url': url}})

    # Sort by match count (higher match count first)
    results.sort(key=lambda x: x['match_count'], reverse=True)

    return results