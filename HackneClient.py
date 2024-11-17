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
            (4, 6),
            (7, 999)
        )
        self.product_links = (
            "https://shorturl.at/kyLC4",
            "https://shorturl.at/iArhm",
            "https://shorturl.at/DtHeC"
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
    
    def get_reccomendation(self, severity) -> str:
        for range, product in zip(self.acne_ranges, self.product_links):
            if range[0] <= severity and severity <= range[1]:
                return f"Based on your facial scan results and skin type, we reccomend you purchase this cleanser, based on your skin condition and type: {product}! Additionally, pair this with the following moisturizers for your daily routine: https://tinyurl.com/am-pm-cream.\n\n"