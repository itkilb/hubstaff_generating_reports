from .requestApi import RequestApi


class Organization(RequestApi):

    # получение всех организаций
    def get_all_organization(self):
        return self._get('organizations').json()

    # получение активности
    def get_all_activities(self, organization_id, date_start, date_end):
        return self._get('organizations/' + str(organization_id) + '/activities/daily',
                         params={'date[start]': date_start, 'date[stop]': date_end}).json()

    # получить все проекты организации
    def get_all_projects(self, organization_id):
        return self._get('organizations/' + str(organization_id) + '/projects').json()
