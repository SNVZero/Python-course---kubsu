from django.db import models


class Pacient(models.Model):
    NamePac = models.CharField("Имя пациента", max_length=70)
    Policy = models.CharField("Номер полиса", max_length=16)
    Birth = models.CharField("Дата рождения",max_length=10)
    Location = models.CharField("Адресс проживания", max_length=70)

    def __str__(self):
        return self.NamePac

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"


class Diagnosis(models.Model):
    Diagnos = models.CharField("Диангоз", max_length=70)
    Severity = models.IntegerField("Степень тяжести")
    diag_policy = models.ForeignKey('Pacient', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Номер полиса')

    def __str__(self):
        return self.Diagnos

    class Meta:
        verbose_name = "Диагноз"
        verbose_name_plural = "Диагнозы"


class Treatment(models.Model):
    MethodOfThreatment = models.CharField("Метод лечения", max_length=70)
    DurationOfTreat = models.CharField("Время лечения", max_length=70)
    treat_policy = models.ForeignKey('Pacient', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Номер полиса')

    def __str__(self):
        return self.MethodOfThreatment

    class Meta:
        verbose_name = "Лечение"
        verbose_name_plural = "Способы лечения"
