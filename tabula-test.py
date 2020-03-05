import tabula

# Read pdf into list of DataFrame
# tabula.io.read_pdf(input_path, output_format=None, encoding='utf-8', java_options=None, pandas_options=None, multiple_tables=True, user_agent=None, **kwargs)
# input_path (str, path object or file-like object) – File like object of tareget PDF file. It can be URL, which is downloaded by tabula-py automatically.
# output_format (str, optional) – Output format for returned object (dataframe or json)
# encoding (str, optional) – Encoding type for pandas. Default: utf-8
# java_options (list, optional) – Set java options. Example ["-Xmx256m"]
# pandas_options (dict, optional) – Set pandas options.

input_path = "./Longitudinal_test.pdf"
list_df = tabula.io.read_pdf(input_path, output_format="dataframe")
df = list_df[0]
print(df.filter(items=['Header 1', 'Header 2']))