class SerialsNumber:
    # class atributes, shared with every instances
    next_serial = 1000

    @classmethod
    def _make_bic_code(cls):
        result = cls.next_serial
        cls.next_serial+=1
        return result


