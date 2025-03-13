import json
from datetime import datetime

def iso_to_milliseconds(iso_timestamp):
    """Converts an ISO 8601 timestamp to milliseconds."""
    dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))  # Convert to datetime
    return int(dt.timestamp() * 1000)  # Convert to milliseconds

def load_json(filepath):
    """Loads JSON data from a file."""
    with open(filepath, "r") as file:
        return json.load(file)

def transform_data(data1, data2):
    """Transforms and merges data from both sources into the target format."""
    unified_data = []

    # Process data-1.json (already in correct format, just rename keys)
    for entry in data1:
        unified_data.append({
            "device_id": entry["device_id"],
            "temperature": entry["temp"],
            "humidity": entry["hum"],
            "timestamp": entry["timestamp"]  # Already in milliseconds
        })

    # Process data-2.json (convert ISO timestamp & rename keys)
    for entry in data2:
        unified_data.append({
            "device_id": entry["id"],  # Rename 'id' to 'device_id'
            "temperature": entry["temperature"],
            "humidity": entry["humidity"],
            "timestamp": iso_to_milliseconds(entry["timestamp"])  # Convert timestamp
        })

    return unified_data

def main():
    """Main function to process telemetry data and output the result."""
    # Load input data
    print("Loading input data...")
    data1 = load_json("data-1.json")
    data2 = load_json("data-2.json")

    # Transform and merge data
    print("Transforming and merging data...")
    result = transform_data(data1, data2)

    # Save to output file
    print("Saving to output.json...")
    with open("output.json", "w") as out_file:
        json.dump(result, out_file, indent=4)
    
    print("Process completed successfully! Check output.json for results.")

if __name__ == "__main__":
    main()
