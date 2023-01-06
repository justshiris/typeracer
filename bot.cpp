#include <iostream>
#include <string>
#include <unistd.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "tesseract/baseapi.h"

#define PATH_TO_TESSERACT "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract" // Set your tesseract location here

int on_click_rx;
int on_click_ry;
int on_click_rx2;
int on_click_ry2;

void shit(void) {
  cv::Mat ss = cv::Mat(cv::Size(abs(on_click_rx - on_click_rx2), abs(on_click_ry - on_click_ry2)), CV_8UC3);
  ss = cv::cvarrToMat(cvGetWindowHandle("Screenshot"), true).colRange(on_click_rx, on_click_rx2).rowRange(on_click_ry, on_click_ry2);
  cv::imwrite("text.png", ss);
  tesseract::TessBaseAPI tess;
  tess.Init(NULL, "eng", tesseract::OEM_DEFAULT);
  tess.SetPageSegMode(tesseract::PSM_SINGLE_BLOCK);
  tess.SetImage((unsigned char*)ss.data, ss.cols, ss.rows, 3, ss.step);
  char* out = tess.GetUTF8Text();
  std::string new_out = std::string(out).replace("|", "I");
  new_out = new_out.replace("\n", " ");

  for (size_t i = 0; i < new_out.length(); i++) {
    std::cout << new_out[i];
    std::cout.flush();
    usleep(70000); // Change to change speed
  }
}

int main(void) {
  cv::namedWindow("Screenshot", cv::WINDOW_AUTOSIZE);
  cv::setMouseCallback("Screenshot", on_click, 0);
  cv::waitKey(0);
  shit();
  return 0;
}

void on_click(int event, int x, int y, int flags, void* userdata) {
  if (event == cv::EVENT_LBUTTONDOWN) {
    on_click_rx = x;
    on_click_ry = y;
  } else if (event == cv::EVENT_LBUTTONUP) {
    on_click_rx2 = x;
    on_click_ry2 = y;
    cv::destroyWindow("Screenshot");
  }
}
