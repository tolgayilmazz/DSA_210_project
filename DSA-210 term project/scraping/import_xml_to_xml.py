import xml.etree.ElementTree as ET
from datetime import datetime

def parse_and_aggregate_health_data_to_xml(input_file, output_file):
    """
    Parses Apple Health XML, aggregates data by day, and outputs to a new XML file.
    """
    aggregated_data = {}

    # Define target types and date range
    target_types = {
        "HKQuantityTypeIdentifierFlightsClimbed": "Flights Climbed",
        "HKQuantityTypeIdentifierActiveEnergyBurned": "Active Energy Burned"
    }
    start_date = datetime(2023, 10, 1)
    end_date = datetime(2024, 6, 30)

    # Parse XML iteratively for efficiency
    for event, elem in ET.iterparse(input_file, events=("end",)):
        if elem.tag == "Record" and elem.get("type") in target_types:
            record_date = datetime.strptime(elem.get("startDate").split()[0], "%Y-%m-%d")
            if start_date <= record_date <= end_date:
                record_type = target_types[elem.get("type")]
                value = float(elem.get("value"))
                day = record_date.strftime("%Y-%m-%d")
                if day not in aggregated_data:
                    aggregated_data[day] = {"Active Energy Burned": 0, "Flights Climbed": 0}
                aggregated_data[day][record_type] += value
        elem.clear()

    # Build new XML tree for aggregated data
    root = ET.Element("AggregatedData")
    for day, values in aggregated_data.items():
        day_element = ET.SubElement(root, "Day", date=day)
        for key, value in values.items():
            ET.SubElement(day_element, key.replace(" ", "")).text = str(value)

    # Write the output XML file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Aggregated data saved to {output_file}")

# Input and output file paths
input_file = "dışa aktarılan.xml"
output_file = "aggregated_health_data321.xml"
parse_and_aggregate_health_data_to_xml(input_file, output_file)
