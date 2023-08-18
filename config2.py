import json

def process_json(json_data):
    common = json_data["common"]
    cases = json_data["cases"]
    
    print("Common:")
    print("Library:", common["lib"])
    print("Data Format:", common["data-format"])
    print("Data Order:", common["data-order"])
    print("Data Type:", common["dtype"])
    print("\nCases:")
    
    for case in cases:
        print("Algorithm:", case["algorithm"])
        print("Dataset:")
        for dataset in case["dataset"]:
            print("  Source:", dataset.get("source", "Unknown"))
            if "type" in dataset:
                print("  Type:", dataset["type"])
            if "n_features" in dataset:
                print("  Features:", dataset["n_features"])
            print("  Training Samples:", dataset["training"]["n_samples"])
            if "testing" in dataset:
                print("  Testing Samples:", dataset["testing"]["n_samples"])
        if "time-method" in case:
            print("Time Method:", case["time-method"])
        if "time-limit" in case:
            print("Time Limit:", case["time-limit"])
        if "n-clusters" in case:
            print("Number of Clusters:", case["n-clusters"])
        if "maxiter" in case:
            print("Max Iterations:", case["maxiter"])
        if "init" in case:
            print("Initialization Method:", case["init"])
        if "tol" in case:
            print("Tolerance:", case["tol"])
        print()


def main():
    with open('skl_config.json', 'r') as file:
        json_data = json.load(file)
    
    processed_data = process_json(json_data)
    return processed_data

if __name__ == "__main__":
    main()

