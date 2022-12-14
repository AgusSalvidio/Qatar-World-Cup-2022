from .promo_code import PromoCode

class PromoCodeManagementSystem:

    def __init__(self):
        self.promo_codes_repo = PromoCode.objects

    def promo_codes(self):
        return self.promo_codes_repo.all()

    def name(self):
        return 'Sistema de Administración de Códigos Promocionales'

    def register(self, promo_code):
        promo_code.save()

    def identified_as(self,promo_code_id,object_class):
        return self.promo_codes_repo.get(id = promo_code_id)

    def unregister(self,promo_code):
        promo_code.delete()

    def assert_there_is_no_promo_code_identified_as(self, code):
        pass

    def update_with(self,promo_code,updated_promo_code):
        if promo_code.code != updated_promo_code.code:
            self.assert_there_is_no_promo_code_identified_as(updated_promo_code.code)
        promo_code.synchronize_with(updated_promo_code)
        promo_code.save()

    def class_knownledge(self):
        return ['PromoCode']