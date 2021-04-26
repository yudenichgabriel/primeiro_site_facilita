from django.db import models
import decimal

# Create your models here.

class company(models.Model):
    name = models.CharField(max_length=255, name='Agência')
    def __str__(self):
        return self.Agência
    class Meta:
        managed = True
        verbose_name = 'Agência'
        verbose_name_plural = 'Agências'

class distribute(models.Model):
    name = models.CharField(max_length=255, name='Fornecedor')
    def __str__(self):
        return self.Fornecedor
    class Meta:
        managed = True
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

class ticket_account(models.Model):
    Conta_vinculada = models.CharField(max_length=255)
    def __str__(self):
        return self.Conta_vinculada
    class Meta:
        managed = True
        verbose_name = 'Conta Vinculada'
        verbose_name_plural = 'Contas vinculadas'

class miles_currency(models.Model):
    name = models.CharField(max_length=50, name='Nome')
    currency = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    currency_model = 'R$'
    def __str__(self):
        return '{} {} {}'.format(self.Nome, self.currency_model, self.currency)
    class Meta:
        managed = True
        verbose_name = 'Valor do milhar'
        verbose_name_plural = 'Valor do milhar'

class card_used(models.Model):
    name = models.CharField(max_length=255, help_text='Somente os últimos digitos', default="NUBANK 0000")
    def __str__(self):
        return self.name

class tickets_list(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data da emissão')
    localizador = models.CharField(max_length=6, unique=True)
    agencia = models.ForeignKey(company, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(distribute, on_delete=models.CASCADE)
    conta_vinculada = models.ForeignKey(ticket_account, on_delete=models.CASCADE)
    milhar = models.ForeignKey(miles_currency, on_delete=models.CASCADE)
    taxas = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    adicional = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cartao = models.ForeignKey(card_used, verbose_name="Cartão Usado", on_delete=models.CASCADE)
    obs = models.TextField(blank=True, null=True)
    anexo = models.FileField(upload_to='bilhetes', max_length=100, blank=True, null=True)
    def total(self):
        get_id_ticket = tickets_list.objects.filter(localizador=(self.localizador)).values_list('id')
        get_id_ticket_int = str(''.join(map(str, get_id_ticket))).replace('(', '').replace(')', '').replace(',', '')

        count_id = ticket_pax.objects.filter(ticket_id=(get_id_ticket_int)).values_list('ticket_id').count()

        miles = ticket_pax.objects.filter(ticket_id=(get_id_ticket_int)).values_list('milhas')
        get_miles_str = (''.join(map(str, miles))).replace('Decimal', '').replace('(', '').replace(')', '').replace("'", "")
        get_miles_count = get_miles_str.split(',')

        count_pax = True
        num_pax = int(count_id)
        num_pax = num_pax - 1
        if num_pax != -1:
            pax1 = float(get_miles_count[num_pax])
            num_pax = num_pax - 1
            totalMiles = pax1
            print(totalMiles, ' pax1')
            if num_pax != -1:
                pax2 = float(get_miles_count[num_pax])
                num_pax = num_pax - 1
                totalMiles = pax1 + pax2
                print(totalMiles, ' pax2')
                if num_pax != -1:
                    pax3 = float(get_miles_count[num_pax])
                    num_pax = num_pax - 1
                    totalMiles = pax1 + pax2 + pax3
                    print(totalMiles, ' pax3')
                    if num_pax != -1:
                        pax4 = float(get_miles_count[num_pax])
                        num_pax = num_pax - 1
                        totalMiles = pax1 + pax2 + pax3 + pax4
                        print(totalMiles, ' pax4')
                        if num_pax != -1:
                            pax5 = float(get_miles_count[num_pax])
                            num_pax = num_pax - 1
                            totalMiles = pax1 + pax2 + pax3 + pax4 + pax5
                            print(totalMiles, ' pax5')
                            if num_pax != -1:
                                pax6 = float(get_miles_count[num_pax])
                                num_pax = num_pax - 1
                                totalMiles = pax1 + pax2 + pax3 + pax4 + pax5 + pax6
                                print(totalMiles, ' pax6')
                                if num_pax != -1:
                                    pax7 = float(get_miles_count[num_pax])
                                    num_pax = num_pax - 1
                                    totalMiles = pax1 + pax2 + pax3 + pax4 + pax5 + pax6 + pax7
                                    print(totalMiles, ' pax7')
                                    if num_pax != -1:
                                        pax8 = float(get_miles_count[num_pax])
                                        num_pax = num_pax - 1
                                        totalMiles = pax1 + pax2 + pax3 + pax4 + pax5 + pax6 + pax7 + pax8
                                        print(totalMiles, ' pax8')
                                        if num_pax != -1:
                                            pax9 = float(get_miles_count[num_pax])
                                            num_pax = num_pax - 1
                                            totalMiles = pax1 + pax2 + pax3 + pax4 + pax5 + pax6 + pax7 + pax8 + pax9
                                            print(totalMiles, ' pax9')
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

        get_miles_currency = self.milhar.currency
        get_taxes = self.taxas
        get_luggage = self.adicional

        sum_A = decimal.Decimal(totalMiles) * get_miles_currency
        sum_B = sum_A + get_taxes + get_luggage

        return 'R$ {}, total de pontos: {}'.format(sum_B, totalMiles)

    def cia(self):
        return self.milhar.Nome
    
    def nome_pax(self):
        get_id_ticket = tickets_list.objects.filter(localizador=(self.localizador)).values_list('id')
        get_id_ticket_int = str(''.join(map(str, get_id_ticket))).replace('(', '').replace(')', '').replace(',', '')

        count_id = ticket_pax.objects.filter(ticket_id=(get_id_ticket_int)).values_list('ticket_id').count()

        get_name_value = ticket_pax.objects.filter(ticket_id=(get_id_ticket_int)).values_list('name')

        get_name_value_str = (''.join(map(str, get_name_value))).replace('(', '').replace(')', '').replace("'", "")
        get_name_value_count = get_name_value_str.split(',')
        
        if int(count_id) > 1:
            count_id = count_id - 1
            return '"{}" e mais {} pax...'.format(get_name_value_count[0], count_id)
        else:
            return get_name_value_count
    
    class Meta:
        managed = True
        verbose_name = 'Lista de emissões'
        verbose_name_plural = 'Lista de emissões'

class ticket_pax(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    eticket = models.CharField(max_length=255, unique=True, blank=True, null=True, name='E-Ticket')
    age = models.CharField(choices=[('Adulto', 'Adulto'),('Criança', 'Criança'),('Bebê', 'Bebê'),], max_length=50, verbose_name='Tipo de passageiro(a)')
    milhas = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Total de Milhas')
    ticket_id = models.ForeignKey(tickets_list, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        verbose_name = 'Passageiro'
        verbose_name_plural = 'Passageiros'