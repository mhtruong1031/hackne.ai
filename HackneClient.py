from ultralytics import YOLO

class HackneClient:
    def __init__(self, model_path: str) -> None:
        self.MODEL_PATH = model_path
        self.model = YOLO(model_path)

        # Fine-tuning Configurables
        self.conf    = 0.275,
        self.iou     = 0.6, 
        self.max_det = 300,
    
        self.acne_ranges = (
            (0, 3),
            (7, 10),
            (7, 1e99)
        )
        self.product_lists = {
            'dry': ("Moisturizer: SKIN1004 Hyalu-Cica Moisture Cream (AM/PM)", "Sunscreen: SKIN1004 Hyalu-Cica Water-Fit Sun Serum SPF50+ PA++++ (AM)"),
            'comb': ("Moisturizer: SKIN1004 Centella Soothing Cream (AM/PM)", "SKIN1004 Hyalu-Cica Water-Fit Sun Serum SPF50+ PA++++ (AM)"),
            'oily': ("Moisturizer: SKIN1004 Poremizing Light Gel Cream", "SKIN1004 Centella Air-Fit Suncream Plus SPF50+ PA++++ (AM)")
        }
        self.cleansers = (
            "Skin1004 Centella Ampoule Foam (AM/PM)",
            "Skin1004 TEA-TRICA BHA FOAM (AM/PM)",
            "Skin1004 TEA-TRICA BHA FOAM (AM/PM)"
        )

    def predict(self, source_path: str):
        results = self.model(
            source  = source_path,
            stream  = True,
            imgsz   = 640,
            conf    = 0.275,
            iou     = 0.6, 
            max_det = 300,
        )

        for result in results:
            return result
    
    def get_reccomendation(self, severity: int, skin_type: str) -> str:
        for range, product in zip(self.acne_ranges, self.cleansers):
            if range[0] <= severity and severity <= range[1]:
                cleanser = product
        
        return (cleanser, self.product_lists[skin_type][0], self.product_lists[skin_type][1])
