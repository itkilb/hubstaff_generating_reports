from hubstaff.api.organization import Organization
from hubstaff.exportData.exportDataToCsv import ExportDataToCsv
import time


def main():
    start_data = "2022-03-07"
    stop_data = "2022-03-20"

    organization = Organization()
    all_organization = organization.get_all_organization()['organizations']

    all_projects = list()
    all_projects_dict = {}
    all_activities = list()
    end_dict = {}

    # получаем все проекты организации
    for item in all_organization:
        all_projects.append(organization.get_all_projects(item['id'])['projects'])

    # формируем проекты как {'id' : 'name_project'}
    for i in range(len(all_projects)):
        for j in range(len(all_projects[i])):
            all_projects_dict[all_projects[i][j]['id']] = all_projects[i][j]['name']

    # получаем всю активность за определенные даты
    for item in all_organization:
        activities = organization.get_all_activities(item['id'], start_data, stop_data)['daily_activities']
        if len(activities) > 0:
            all_activities.append(activities)

    formatting_all_activities = {}

    # форматирование активности
    for item in all_activities:
        for i in item:
            if i['date'] not in formatting_all_activities:
                formatting_all_activities[i['date']] = {}
            formatting_all_activities[i['date']][i['project_id']] = i

    # форматирование конечного словаря  {"2021-09-08": {"project1": 26909, "project2": 514}}
    for i in formatting_all_activities:
        end_dict[i] = {}
        for j in formatting_all_activities[i]:
            for apd in all_projects_dict:
                if apd == j:
                    end_dict[i][all_projects_dict[apd]] = time.strftime("%H:%M:%S", time.gmtime(
                        int(formatting_all_activities[i][j]['billable'])))

    # приводим словарь к массиву вида ['2021-09-08', 'project1', 26909, 'project2', 514 ...]
    result = []
    for i in end_dict:
        m = [i]
        for j in end_dict[i]:
            m.append(j)
            m.append(end_dict[i][j])
        result.append(m)

    result.sort()
    ExportDataToCsv(result).export_data()
