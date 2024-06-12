import apache_beam as beam

def run():
    p1 = beam.Pipeline()
    voos = (
        p1
        | "Read Data" >> beam.io.ReadFromText("gs://<your-bucket-name>/california_housing_test.csv", skip_header_lines=1)
        | "Split by comma" >> beam.Map(lambda record: record.split(','))
        | "Print Results" >> beam.Map(print)
        | "Write Results" >> beam.io.WriteToText("gs://<your-bucket-name>/california_housing_test_raj.csv")
    )
    p1.run().wait_until_finish()

if __name__ == '__main__':
    run()
