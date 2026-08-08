import os

class Config:
    ONE_C_BASE_URL = os.getenv("ONE_C_BASE_URL", "http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1")
    ONE_C_LOGIN = os.getenv("ONE_C_LOGIN", "FitnessKit")
    ONE_C_PASSWORD = os.getenv("ONE_C_PASSWORD", "vY0xodyg")
    ONE_C_REQUEST_ID = "e1477272-88d1-4acc-8e03-7008cdedc81e" #Для GetSpecialistList
    DEFAULT_CLUB_ID = os.getenv("DEFAULT_CLUB_ID", "59115d1e-9052-11eb-810c-6eae8b56243b")
