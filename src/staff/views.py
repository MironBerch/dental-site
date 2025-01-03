from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from staff.services import (
    get_all_staff,
    get_staff_by_slug,
    get_staff_by_stage,
    get_staff_by_stage_title,
)


class StaffView(TemplateResponseMixin, View):
    template_name = 'staff/list.html'

    def get(self, request: HttpRequest):
        staff = get_all_staff()
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'managers':  staff.get('Руководитель', ''),
                'administrators': staff.get('Администратор', ''),
                'medics': staff.get('Мед персонал', ''),
                'junior_medics': staff.get('Младщий мед персонал', ''),
            },
        )


class StaffByStageView(TemplateResponseMixin, View):
    template_name = 'staff/stage.html'

    def get(self, request: HttpRequest, stage: str):
        all_staff = get_all_staff()
        staff = get_staff_by_stage(stage)
        return self.render_to_response(
            context={
                'page_title': get_staff_by_stage_title(stage),
                'active_page': 'staff',
                'staff': staff,
                'managers':  all_staff.get('Руководитель', ''),
                'administrators': all_staff.get('Администратор', ''),
                'medics': all_staff.get('Мед персонал', ''),
                'junior_medics': all_staff.get('Младщий мед персонал', ''),
            },
        )


class StaffDetailView(TemplateResponseMixin, View):
    template_name = 'staff/detail.html'

    def get(self, request: HttpRequest, stage: str, slug: str):
        all_staff = get_all_staff()
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'staff': get_staff_by_slug(slug=slug),
                'managers':  all_staff.get('Руководитель', ''),
                'administrators': all_staff.get('Администратор', ''),
                'medics': all_staff.get('Мед персонал', ''),
                'junior_medics': all_staff.get('Младщий мед персонал', ''),
            },
        )
