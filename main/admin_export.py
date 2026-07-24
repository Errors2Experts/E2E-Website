from openpyxl import Workbook
from django.http import HttpResponse


class ExportExcelAdmin:

    actions = ["export_to_excel"]

    def export_to_excel(self, request, queryset):

        workbook = Workbook()
        worksheet = workbook.active

        model = self.model

        fields = [field.name for field in model._meta.fields]

        # Header
        worksheet.append(fields)

        # Data
        for obj in queryset:
            row = []

            for field in fields:
                value = getattr(obj, field)

                # ForeignKey
                if hasattr(value, "__str__"):
                    value = str(value)

                row.append(value)

            worksheet.append(row)

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        response["Content-Disposition"] = (
            f'attachment; filename="{model._meta.model_name}.xlsx"'
        )

        workbook.save(response)

        return response

    export_to_excel.short_description = "📥 Export Selected to Excel"
