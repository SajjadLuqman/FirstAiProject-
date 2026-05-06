# queries.py

def get_total_balance_query():
    return """
    SELECT 
        COALESCE(SUM(Debit * Rate), 0) AS TotalDebit,
        COALESCE(SUM(Credit * Rate), 0) AS TotalCredit
    FROM JournalEntries WITH (NOLOCK)
    WHERE IsDelete = 0
    """


def get_branch_balance_query():
    return """
    SELECT 
        BranchId,
        COALESCE(SUM(Debit * Rate), 0) AS TotalDebit,
        COALESCE(SUM(Credit * Rate), 0) AS TotalCredit,
        COALESCE(SUM(Debit * Rate), 0) - COALESCE(SUM(Credit * Rate), 0) AS Difference
    FROM JournalEntries WITH (NOLOCK)
    WHERE IsDelete = 0
    GROUP BY BranchId
    """


def get_branch_currency_balance_query():
    return """
    SELECT 
        BranchId,
        CurrencyId,
        COALESCE(SUM(Debit * Rate), 0) AS TotalDebit,
        COALESCE(SUM(Credit * Rate), 0) AS TotalCredit,
        COALESCE(SUM(Debit * Rate), 0) - COALESCE(SUM(Credit * Rate), 0) AS Difference
    FROM JournalEntries WITH (NOLOCK)
    WHERE IsDelete = 0
    GROUP BY BranchId, CurrencyId
    """


def get_branch_currency_year_balance_query(tolerance=0.01):
    return f"""
    SELECT 
        BranchId,
        CurrencyId,
        YearId,
        COALESCE(SUM(Debit * Rate), 0) AS TotalDebit,
        COALESCE(SUM(Credit * Rate), 0) AS TotalCredit,
        COALESCE(SUM(Debit * Rate), 0) - COALESCE(SUM(Credit * Rate), 0) AS Difference
    FROM JournalEntries WITH (NOLOCK)
    WHERE IsDelete = 0
    GROUP BY BranchId, CurrencyId, YearId
    HAVING ABS(
        COALESCE(SUM(Debit * Rate), 0) - 
        COALESCE(SUM(Credit * Rate), 0)
    ) > {tolerance}
    """


def get_unbalanced_voucher_query(tolerance=0.01):
    return f"""
    SELECT 
        BranchId,
        CurrencyId,
        YearId,
        VoucherNo,
        VoucherTypeId,
        VoucherNoTableId,
        VoucherDate,
        COALESCE(SUM(Debit * Rate), 0) AS TotalDebit,
        COALESCE(SUM(Credit * Rate), 0) AS TotalCredit,
        COALESCE(SUM(Debit * Rate), 0) - COALESCE(SUM(Credit * Rate), 0) AS Difference
    FROM JournalEntries WITH (NOLOCK)
    WHERE IsDelete = 0
    GROUP BY 
        BranchId,
        CurrencyId,
        YearId,
        VoucherNo,
        VoucherTypeId,
        VoucherNoTableId,
        VoucherDate
    HAVING ABS(
        COALESCE(SUM(Debit * Rate), 0) - 
        COALESCE(SUM(Credit * Rate), 0)
    ) > {tolerance}
    ORDER BY ABS(
        COALESCE(SUM(Debit * Rate), 0) - 
        COALESCE(SUM(Credit * Rate), 0)
    ) DESC
    """