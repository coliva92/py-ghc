import ghc
import ghc.competition as cmp




if __name__ == '__main__':
  in_desc = [
    # llenar con la descripcion de los datos de entrada
  ]
  in_filename, out_filename = ghc.get_args(cmp.PROBLEM_NAME, cmp.YEAR)
  in_data = ghc.read_input_file(in_filename, in_desc)
  # procesar los datos de entrada segun el problema de la competencia
  out_data = None
  cmp.write_output_file(out_filename, out_data)
