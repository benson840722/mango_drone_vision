import numpy as np
import cv2

def update(val=0):
    stereo.setBlockSize(cv2.getTrackbarPos('window_size', 'disparity'))
    stereo.setUniquenessRatio(cv2.getTrackbarPos('uniquenessRatio', 'disparity'))
    stereo.setSpeckleWindowSize(cv2.getTrackbarPos('speckleWindowSize', 'disparity'))
    stereo.setSpeckleRange(cv2.getTrackbarPos('speckleRange', 'disparity'))
    stereo.setDisp12MaxDiff(cv2.getTrackbarPos('disp12MaxDiff', 'disparity'))
    # =============================================================================
    #     cv2.setTrackbarPos('滑桿名稱','視窗名稱', val)
    #     val 滑桿預設值
    # =============================================================================
    print ('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
    #print(disp)
    cv2.imshow('left', imgL)
    cv2.imshow('right', imgR)
    cv2.imshow('disparity', (disp-min_disp)/num_disp)
    
 
if __name__ == "__main__":
    window_size = 5 #SADWindowSize：SAD窗口大小，容许范围是[1,11]，一般应该在 3x3 至 11x11 之间，参数必须是奇数，int 型
    min_disp = 6 #原本是16
    num_disp = 54-min_disp #原本192
    blockSize = window_size
    uniquenessRatio = 5
    speckleRange = 1 #12
    speckleWindowSize = 50 #原本3
    disp12MaxDiff = 50
    P1 = 600  #請參閱 stereo_match.cpp 示例，其中顯示了一些相當不錯的 P1值為 (8*number_of_image_channels*SADWindowSize*SADWindowSize)
    P2 = 2400 # (32*number_of_image_channels*SADWindowSize*SADWindowSize) 
     
    imgL = cv2.imread('left.jpg')
    imgR = cv2.imread('right.jpg')
 
    
    stereo = cv2.StereoSGBM_create(
        minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = window_size,
        uniquenessRatio = uniquenessRatio,
        speckleRange = speckleRange,
        speckleWindowSize = speckleWindowSize,
        disp12MaxDiff = disp12MaxDiff,
        P1 = P1,
        P2 = P2)
    cv2.namedWindow('disparity')
    cv2.createTrackbar('speckleRange', 'disparity', speckleRange, 10, update)    
    cv2.createTrackbar('window_size', 'disparity', window_size, 13, update)
    cv2.createTrackbar('speckleWindowSize', 'disparity', speckleWindowSize, 200, update)
    cv2.createTrackbar('uniquenessRatio', 'disparity', uniquenessRatio, 20, update)
    cv2.createTrackbar('disp12MaxDiff', 'disparity', disp12MaxDiff, 100, update)
    # =============================================================================
    #     cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
    #     min 最小值 ( 最小為 0，不可為負值 )
    #     max 最大值
    #     fn 滑桿數值改變時要執行的函式
    # =============================================================================
    '''
    cv2.createStereoSGBM(minDisparity, numDisparities, blockSize[, P1[, P2[, disp12MaxDiff[, preFilterCap[, uniquenessRatio[, speckleWindowSize[, speckleRange[, mode]]]]]]]]) → retval
    Parameters: 
        minDisparity – 最小可能差異值。 通常情況下，它為零，但有時校正算法會移動圖像，因此需要相應地調整此參數。
        numDisparities – 最大視差減去最小視差。 該值始終大於零。 在當前實現中，此參數必須能被 16 整除。
        blockSize – 匹配的塊大小。 它必須是一個奇數 >=1 。 通常，它應該在 3..11 範圍內的某個地方。
        P1 – 控制視差平滑度的第一個參數。 見下文。
        P2 – 控制視差平滑度的第二個參數。 值越大，視差越平滑。 P1 是對相鄰像素之間的視差變化正負 1 的懲罰。 P2 是對相鄰像素之間視差變化超過 1 的懲罰。 該算法要求 P2 > P1 。 
        disp12MaxDiff – 左右差異檢查中的最大允許差異（以整數像素為單位）。 將其設置為非正值以禁用檢查。
        preFilterCap – 預過濾圖像像素的截斷值。 該算法首先計算每個像素的 x 導數，並按 [-preFilterCap, preFilterCap] 間隔裁剪其值。 結果值被傳遞給 Birchfield-Tomasi 像素成本函數。
        uniquenessRatio – 以百分比表示的最佳（最小）計算成本函數值應“贏得”第二最佳值以認為找到的匹配正確的百分比。 通常，5-15 範圍內的值就足夠了。
        speckleWindowSize – 平滑視差區域的最大尺寸，以考慮其噪聲斑點並使其失效。 將其設置為 0 以禁用斑點過濾。 否則，將其設置在 50-200 範圍內的某個位置。
        speckleRange – 每個連接組件內的最大視差變化。 如果你做斑點過濾，將參數設置為正值，它會隱式乘以 16。通常，1 或 2 就足夠了
        mode –將其設置為 StereoSGBM::MODE_HH 以運行全面的二次動態規划算法。 它將消耗 O(W*H*numDisparities) 字節，這對於 640x480 立體圖像來說很大，對於高清尺寸的圖片來說很大。 默認情況下，它設置為 false 。   
    '''
    #global stereo
    
    
    update()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
