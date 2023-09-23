class LoanConstants:
    UNIQUE_ID_PREFIX = "BOFSLN"
    TDS_INTEREST_RATE = 10

    class REPAYMENT_STRUCTURE:
        MONTHLY = "monthly"
        QUATERLY = "quaterly"
        ANNUAL = "annual"
        SEMI_ANNUALY = "semi_annualy"
        BULLET = "bullet_payment"
        STRUCTURED = "structured"

        MONTHLY_PAY_MONTH = 1
        QUATERLY_PAY_MONTH = 3
        ANNUAL_PAY_MONTH = 12
        STRUCTURED_PAY_MONTH = 0
        BULLET_PAY_MONTH = 1
        SEMI_ANNUAL_PAY_MONTH = 6

        STRUCTURED_PAYMENT = "Structured"
        NON_STRUCTURED_PAYMENT = "Standard"

    class AMOUNT_ROUND_OFF:
        ROUND_OFF = 5

    class GET_LOAN_INFO_FROM:
        LOAN_NUMBER = "loan_number",
        SANCTION_NUMBER = "sanctioned_letter_number"
        USER_ID = "user_id"

    class TYPE_INTEREST:
        FIXED = "fixed"
        VARIABLE = "variable"

    class ERROR_MESSAGE:
        MESSAGE = "Contact Developers or Please Try Again Later"
