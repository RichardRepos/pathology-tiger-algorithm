import gcapi  # pip install gcapi

your_algorithm_slug = "nnunet_segmentation_for_detection"           # <--- CHANGE THIS
client = gcapi.Client(token="0efc24961ab263566ba64ff87579a2079cffc932b366a977b96976f60ca4a385")                           # <--- CHANGE THIS, more information about the token please see this link: https://grand-challenge.org/documentation/what-can-gc-api-be-used-for/

job = client.run_external_job(
    algorithm=your_algorithm_slug,
    inputs={
        # 104S (from the tils training subset)
        "generic-medical-image": "https://grand-challenge.org/api/v1/cases/images/18a9e579-34bd-43b7-ac42-61541fb35156/",
        # 104S_rois (similar rois as expected in L1)  
        "generic-overlay": "https://grand-challenge.org/api/v1/cases/images/e676fdaa-719e-4050-81b7-4724fed69c52/"
    }
)
# More information about gcapi please see this link: https://grand-challenge.org/documentation/grand-challenge-api/

###
print(job["status"] )
###