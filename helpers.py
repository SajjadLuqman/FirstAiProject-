from IPython.display import display, HTML

def show_balance_result(df, title):
    if df.empty:
        display(HTML(f"<b style='color:green;'>{title}: balanced</b>"))
    else:
        display(HTML(f"<b style='color:red;'>{title}: unbalanced records found</b>"))
        display(df)