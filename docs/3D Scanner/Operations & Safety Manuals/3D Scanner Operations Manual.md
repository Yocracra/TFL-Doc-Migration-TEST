---
title: "3D Scanner Operations Manual"
source_id: "1esRY3jfmFp81NKIGSTxYHIxJP2jztSMbBimA8Ux1l8E"
modified: "2026-04-12T22:40:57.758Z"
---

3D Scanner Operations Manual

Machine Name: Creality Raptor Pro 3D Scanner

Location: The Fab Lab

Version: v0.6

Last Updated: 03/27/2026

Responsible Student Worker: Aidan Stewart

Linked Safety Manual: [Praxis PS 3D Scanner Safety Manual](<3D Scanner Safety Manual.md>)

## 1\. What This Machine Is For

Use this machine to:

  * Gather point-cloud and photogrammetry data of real-world geometry
  * Generate texture-mapped mesh models of an object(s) using gathered point-cloud data



## 2\. What This Machine Is Not For

This machine is not made for:

  * Real-time LiDAR/infrared scanning (for example, on an autonomous robot)
  * Geometry or tolerance smaller than 0.1mm
  * Laser pointer



## 3\. What You Need Before You Start

Before operating this machine, ensure:

  * You have read and understood the Safety Manual
  * You have a clear space to maneuver the scanner around the object
  * The plane the object is resting on is not black, reflective, or transparent
  * The object you’re scanning is not black, reflective, or transparent. If it is, refer to Section 8.
  * You have an [adequately-powered](<https://www.google.com/url?q=https://wiki.creality.com/en/3d-scanner/tutorials/general/performance&sa=D&source=editors&ust=1776804251074397&usg=AOvVaw15hvZPk3OtGd3dRYfeM59x>) laptop or other computer next to the scanning area. Also be aware of the amount of disk space left on your computer. These files get decently large.



## 4\. Machine Overview![](../../assets/images/3d_scanner_operation_fa6423e291.png)

  1. 3D Scanning Camera: The cameras used to capture geometric data
  2. Color Camera: The cameras used to capture color textures to map to the scanned model
  3. DOE Projector: Projects the structured infrared light pattern onto the object
  4. Parallel Laser: Projects the parallel laser lines
  5. Cross Laser: Projects the crossed laser lines
  6. Color Supplemental Light: Illuminators for color camera (basically just flash)
  7. Type-C Data Interface: Interface to the computer and power supply
  8. View Zoom Out/In: Increase/decrease FOV on the scan preview window
  9. Brightness/Exposure +/-: Manual adjustment of scanning camera’s brightness
  10.  Works equivalently to the start/pause scanning button in CrealityScan



## 5\. Basic Operating Workflow

For additional reference, please refer to the Raptor Pro’s [user manual](<https://www.google.com/url?q=https://wiki.creality.com/en/3d-scanner/raptorpro/manual&sa=D&source=editors&ust=1776804251075881&usg=AOvVaw2u3NG3iWkIB9FiLTmgf6Hy>).

When handling the scanner, take extreme care. Avoid smudging the glass. If you do, please clean it off with the included microfiber rag.

### 5.1 Start-Up

  1. Slide the American wall plug adapter into the DC power supply.
  2. Insert the USB Type-C port into the Type-C Data Interface (7) and hand-tighten the screws.
  3. Connect the female and male ends of the DC power supply cable together.
  4. Plug the USB Type-A data cable into a USB 3.0 port on your computer.
  5. Plug the DC power supply into a standard 110V wall outlet.
  6. Start the CrealityScan 4 software. Once you get past whatever popups and dialogues, it should say “Scanner Connected” at the top left.



### 5.2 Running a Job

  1. In CrealityScan 4, click “New Project”, and complete the dialogue.
  2. At the top center of the screen, enter the Calibration tab. Follow the on-screen instructions to complete calibration. You really only need to perform calibration once.
  3. Once calibration is complete, go back to the scan tab.
  4. Choose your desired mode—blue laser or infrared. If you’re unsure, hover over the “🛈” tooltips for more information.
  5. Customize the additional settings in the sidebar to your needs. If you’re using markers, I recommend doing a “Global Markers” scan first. It seems to do a better job of detecting markers than the actual scan modes, and having all the markers mapped before scanning will make scanning a much easier process.
  6. Click “Preview”, or click the center button on the scanner.
  7. Get an idea of how far you need to be from the target object. The colored sidebar will help you out here, though it can get confused.
  8. Click “Start” to begin scanning. Watch as the point cloud is populated in real-time, and perform your scan as necessary. Keep in mind that while you scan, the point cloud is loaded to RAM. The number of points you can scan (and post-process later on) is limited by your available RAM. If you need to split the object up into multiple scans, you can store multiple scans in the same project and use CrealityScan to automatically align the scans together.



### 5.3 End-of-Job / Shutdown

  1. When you’re done scanning, click “Finish”. 
  2. To run post-processing on your scans, enter the “Mesh Processing” tab. You can manually edit and delete areas of the mesh, and you can use automatic tools for smoothing, simplifying, and fixing your mesh. Refer to Section 9.
  3. Close the file, close CrealityScan, and unplug all the cables you put together in 5.1.



## 6\. User Responsibilities After Use

After using this machine, you must:

  * Ensure the lens is clean
  * Place all items from the box as you found it. If something seems wrong, please ask Fab Lab staff. If there’s not many marker stickers left in the kit, let the lab assistant know.

* * *




## 7\. Stop Conditions

Stop immediately and notify Fab Lab staff if:

  * You drop, hit, or otherwise damage the 3D scanner
  * You are unsure how to proceed



Do not attempt to troubleshoot major issues yourself.

## 8\. Common Issues & What To Do

  * Issue: CrealityScan crashes, freezes, or your scanner loses connection  
Action: Unless something looks seriously wrong, it happens. Close CrealityScan, unplug and replug the scanner, and start CrealityScan again.
  * Issue: Problems keeping the scanner from losing track  
Action: Change your tracking mode to a more effective method. Use the “🛈” tooltips to help decide. If you’re still having issues, consider adding more markers and possibly switching to marker-based tracking. Otherwise, ensure you aren’t trying to scan a black, reflective, or transparent item. If so, you may need to apply a coat of scanning spray to the item.
  * Issue: Object being scanned has black, transparent, or reflective features.  
Action: Take your object to the sink, thoroughly shake the scanning spray to mix it, and apply a coat of spray to the scanning surface. Don’t over-apply—only once it completely evaporates will you suddenly see the effect of the scanning spray. The spray is simply a mixture of isopropanol and talcum powder.



## 9\. Post-Processing

Depending on your use case, post-processing may be the bulk of your work. For specialized, high-power GUI-based post-processing, the following software are great choices.

  * [MeshLab](<https://www.google.com/url?q=https://www.meshlab.net/&sa=D&source=editors&ust=1776804251081327&usg=AOvVaw2eVk0cBUTJOQfctxQ-7Bsz>) (Free and Open Source)
  * [Blender](<https://www.google.com/url?q=https://www.blender.org/&sa=D&source=editors&ust=1776804251081457&usg=AOvVaw0qn6-jc01EJsdcIiEgTg1V>) (Free and Open Source)
  * [CloudCompare](<https://www.google.com/url?q=https://www.cloudcompare.org/&sa=D&source=editors&ust=1776804251081554&usg=AOvVaw0pRTZbhdZ2nglrpAwKsBum>) (Free and Open Source)
  * [Autodesk Meshmixer](<https://www.google.com/url?q=https://meshmixer.org/&sa=D&source=editors&ust=1776804251081683&usg=AOvVaw1QACJsKMk0TASpL5TzlFLh>) (Free, Proprietary) (⚠️ Depreciated since 2023) (Linked website is unofficial)



Luckily, CrealityScan provides some decent post-processing tools directly in the application. To get started, after finishing your scan(s), return to the project’s main page.

![](../../assets/images/3d_scanner_operation_7094e72915.png)

Use the editing toolbar to remove excess data points. [Shift] [LMB] selects, while [CTRL] [LMB] deselects. 

Tip for removing most excess data:

  1. Enable “Penetrate Selection” in the toolbar.
  2. Switch to orthographic view by right-clicking anywhere in the viewport.
  3. Position camera above the model and use the lasso tool to select only the model.
  4. Click the “Invert Selection” tool.
  5. Click the “Delete Selection” tool.
  6. Click “Save Edit”.



![](../../assets/images/3d_scanner_operation_4c8658d219.png)

To process the scanned data into a mesh, use the “Fusion” tool. Once processed, again ensure there’s no excess geometry. You can now remove the reusable markers from your object.

To perform advanced post-processing on an object, switch to the “Mesh Processing” tab.

## 10\. External Resources

For more detailed information, refer to:

  * The Raptor Pro’s [user manual](<https://www.google.com/url?q=https://wiki.creality.com/en/3d-scanner/raptorpro/manual&sa=D&source=editors&ust=1776804251083235&usg=AOvVaw109a2jWRLiBQ1H6L6dEam9>) (Creality Wiki)



## 11\. Questions or Help

If you have questions or need assistance at any point, ask a Fab Lab staff member. Staff are always present during operating hours.

* * *

End of Operations Manual