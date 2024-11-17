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
            'dry': ("SKIN1004 Hyalu-Cica Moisture Cream (AM/PM)", "SKIN1004 Hyalu-Cica Water-Fit Sun Serum SPF50+ PA++++ (AM)"),
            'comb': ("SKIN1004 Centella Soothing Cream (AM/PM)", "SKIN1004 Hyalu-Cica Water-Fit Sun Serum SPF50+ PA++++ (AM)"),
            'oily': ("SKIN1004 Poremizing Light Gel Cream", "SKIN1004 Centella Air-Fit Suncream Plus SPF50+ PA++++ (AM)")
        }
        self.product_links = {
            'dry': ("https://www.amazon.com/SKIN1004-Madagascar-Centella-Hyalu-Cica-Moisture/dp/B09XKFFQQX/ref=sr_1_1?sr=8-1", "https://www.amazon.com/Hyalu-CICA-Water-fit-Serum-Prostar-Safe/dp/B0D362MFP1/ref=sr_1_1?sr=8-1"),
            'comb': ("https://www.amazon.com/Madagascar-Centella-Soothing-Quadruple-Strengthens/dp/B09B221Q7K/ref=sr_1_2?sr=8-2", "https://www.amazon.com/Hyalu-CICA-Water-fit-Serum-Prostar-Safe/dp/B0D362MFP1/ref=sr_1_1?sr=8-1"),
            'oily': ("https://www.amazon.com/SKIN1004-Madagascar-Centella-Poremizing-Irritated/dp/B0BSP1Y2BH/ref=sr_1_1?sr=8-1", "https://www.amazon.com/Skin1004-Centella-Line-Air-fit-Suncream/dp/B09JDXC8PM/ref=sr_1_1?sr=8-1")
        }
        self.cleansers = (
            "Skin1004 Centella Ampoule Foam (AM/PM)",
            "Skin1004 TEA-TRICA BHA FOAM (AM/PM)",
            "Skin1004 TEA-TRICA BHA FOAM (AM/PM)"
        )
        self.cleanser_links = (
            "https://www.amazon.com/SKIN1004-Madagascar-Centella-Cleanser-Surfactant/dp/B09JBJDFHH/ref=sr_1_1?sr=8-1",
            "https://www.amazon.com/SKIN1004-Madagascar-Tea-Trica-Professional-Acne-prone/dp/B0B7XFYR23/ref=sr_1_1?sr=8-1",
            "https://www.amazon.com/SKIN1004-Madagascar-Tea-Trica-Professional-Acne-prone/dp/B0B7XFYR23/ref=sr_1_1?sr=8-1",
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
        for i, range in enumerate(self.acne_ranges):
            if range[0] <= severity and severity <= range[1]:
                cleanser      = self.cleansers[i]
                cleanser_link = self.cleanser_links[i]
        
        return ((cleanser, self.product_lists[skin_type][0], self.product_lists[skin_type][1]), (cleanser_link, self.product_links[skin_type][0], self.product_links[skin_type][0]))
