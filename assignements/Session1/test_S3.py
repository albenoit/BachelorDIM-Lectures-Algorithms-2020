# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:46:18 2020

@author: derbaghc
"""

import cv2
import numpy as np
import S3_imgproc_tools as main
import pytest

# =============================================================================
# Tests pour la fonction de déclenchements d'erreurs
# =============================================================================
def test_type_errors_tuNone():
    ##Je m'assure que je reçois bien la ValueError
    with pytest.raises(AttributeError):
        main.type_errors(None)
    

def test_type_errors_tuArray():
    with pytest.raises(AttributeError):
        main.type_errors(1)    

    
def test_type_errors_tuuint8():
    with pytest.raises(TypeError):
        main.type_errors(np.zeros((2, 2), dtype=np.float32))    

