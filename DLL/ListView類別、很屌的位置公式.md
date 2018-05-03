
# C#語法
*****  
ListView類別、很屌的位置公式  
*****  
+ ### ListView 類別  	
	+ View  
		1、LargeIcon：每個項都顯示為一個最大化圖標，在它的下面有一個標籤。  
		2、SmallIcon：每個項都顯示為一個小圖標，在它的右邊帶一個標籤。  
		3、List：每個項都顯示為一個小圖標，在它的右邊帶一個標籤。各項排列在列中，沒有列標頭。  
		4、Details：可以顯示任意的列，但只有第一列可以包含一個小圖標和標籤，其它的列項只能顯示文字信息，有列表頭。  
		5、Tile：每個項都顯示為一個完整大小的圖標，在它的右邊帶項標籤和子項信息。 （只有Windows XP 和 Windows Server 2003 系列支持）  
	+ Clear 方法 ()  
	```
	listView1.Clear();		//連標題列都清空
	listView1.Items.Clear();	//將ListView中的數據清空
	```
	+ Insert
	```
	listView1.Items.Insert(0, item1);   //Add the items to the ListView.    // to the top
	```
	
	```
	// Create a new ListView control.
	ListView listView1 = new ListView();
	listView1.Bounds = new Rectangle(new Point(10,10), new Size(300,200));

	// Set the view to show details.
	listView1.View = View.Details;
	// Allow the user to edit item text.
	listView1.LabelEdit = true;
	// Allow the user to rearrange columns.
	listView1.AllowColumnReorder = true;
	// Display check boxes.
	listView1.CheckBoxes = true;
	// Select the item and subitems when selection is made.
	listView1.FullRowSelect = true;
	// Display grid lines.
	listView1.GridLines = true;
	// Sort the items in the list in ascending order.
	listView1.Sorting = SortOrder.Ascending;

	// Create three items and three sets of subitems for each item.
	ListViewItem item1 = new ListViewItem("item1",0);
	// Place a check mark next to the item.
	item1.Checked = true;
	item1.SubItems.Add("1");
	item1.SubItems.Add("2");
	item1.SubItems.Add("3");
	ListViewItem item2 = new ListViewItem("item2",1);
	item2.SubItems.Add("4");
	item2.SubItems.Add("5");
	item2.SubItems.Add("6");
	ListViewItem item3 = new ListViewItem("item3",0);
	// Place a check mark next to the item.
	item3.Checked = true;
	item3.SubItems.Add("7");
	item3.SubItems.Add("8");
	item3.SubItems.Add("9");

	// Create columns for the items and subitems.
	// Width of -2 indicates auto-size.
	listView1.Columns.Add("Item Column", -2, HorizontalAlignment.Left);
	listView1.Columns.Add("Column 2", -2, HorizontalAlignment.Left);
	listView1.Columns.Add("Column 3", -2, HorizontalAlignment.Left);
	listView1.Columns.Add("Column 4", -2, HorizontalAlignment.Center);

	//Add the items to the ListView.
        listView1.Items.AddRange(new ListViewItem[]{item1,item2,item3});

	// Create two ImageList objects.
	ImageList imageListSmall = new ImageList();
	ImageList imageListLarge = new ImageList();

	// Initialize the ImageList objects with bitmaps.
	imageListSmall.Images.Add(Bitmap.FromFile("C:\\MySmallImage1.bmp"));
	imageListSmall.Images.Add(Bitmap.FromFile("C:\\MySmallImage2.bmp"));
	imageListLarge.Images.Add(Bitmap.FromFile("C:\\MyLargeImage1.bmp"));
	imageListLarge.Images.Add(Bitmap.FromFile("C:\\MyLargeImage2.bmp"));

	//Assign the ImageList objects to the ListView.
	listView1.LargeImageList = imageListLarge;
	listView1.SmallImageList = imageListSmall;

	// Add the ListView to the control collection.
	this.Controls.Add(listView1);
	```
+ ### 很屌的位置公式  
	我自己弄得，很屌喔，非常數學，來做個筆記  
	```
	// 中間
	int picX = (2 * firstX + (labelW + gap) * (global.col)) / 2 - pic_loading.Width / 2;
	int picY = 2 * firstY + (labelH + gap) * (global.row-1)  + gap + pic_loading.Height;
	pic_loading.Location = new Point(picX, picY);
	// 右邊    
	int picboxX = (firstX + (labelW + gap) * (global.col) - gap - pictureBox1.Width);
	pictureBox1.Location = new Point(picboxX, picY);
	```
	
*****
[ListView 類別](https://msdn.microsoft.com/zh-tw/library/system.windows.forms.listview(v=vs.110).aspx)  
[ListView 用法詳解](https://blog.csdn.net/chen_zw/article/details/7910324)  

