import apache_beam as beam

p1 = beam.Pipeline()
voos =(p1
       | "import Data" >> beam.io.ReadFromText("california_housing_test.csv", skip_header_lines=1)
       | "Split by comma" >> beam.Map(lambda record: record.split(','))
       |"Print Results" >> beam.Map(print)
       | "Write Results" >> beam.io.WriteToText("gs://dagoutput/california_housing_test_raj.csv")
      )
p1.run()
