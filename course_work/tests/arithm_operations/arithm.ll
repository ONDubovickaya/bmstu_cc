; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca i32
  %".3" = alloca [34 x i8]
  store [34 x i8] c"\0a=====Start test assignment=====\0a\00", [34 x i8]* %".3"
  %".5" = getelementptr [34 x i8], [34 x i8]* %".3", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5")
  %".7" = load i32, i32* %".2"
  store i32 1, i32* %".2"
  %".9" = load i32, i32* %".2"
  %".10" = alloca [8 x i8]
  store [8 x i8] c"a = %d\0a\00", [8 x i8]* %".10"
  %".12" = getelementptr [8 x i8], [8 x i8]* %".10", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".9")
  %".14" = load i32, i32* %".2"
  %".15" = load i32, i32* %".2"
  %".16" = add i32 %".15", 1
  store i32 %".16", i32* %".2"
  %".18" = load i32, i32* %".2"
  %".19" = alloca [19 x i8]
  store [19 x i8] c"a = a + 1, a = %d\0a\00", [19 x i8]* %".19"
  %".21" = getelementptr [19 x i8], [19 x i8]* %".19", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %".18")
  %".23" = load i32, i32* %".2"
  %".24" = load i32, i32* %".2"
  %".25" = sub i32 %".24", 1
  store i32 %".25", i32* %".2"
  %".27" = load i32, i32* %".2"
  %".28" = alloca [19 x i8]
  store [19 x i8] c"a = a - 1, a = %d\0a\00", [19 x i8]* %".28"
  %".30" = getelementptr [19 x i8], [19 x i8]* %".28", i32 0, i32 0
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %".27")
  %".32" = load i32, i32* %".2"
  %".33" = load i32, i32* %".2"
  %".34" = mul i32 %".33", 2
  store i32 %".34", i32* %".2"
  %".36" = load i32, i32* %".2"
  %".37" = alloca [19 x i8]
  store [19 x i8] c"a = a * 2, a = %d\0a\00", [19 x i8]* %".37"
  %".39" = getelementptr [19 x i8], [19 x i8]* %".37", i32 0, i32 0
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".36")
  %".41" = load i32, i32* %".2"
  %".42" = load i32, i32* %".2"
  %".43" = sdiv i32 %".42", 2
  store i32 %".43", i32* %".2"
  %".45" = load i32, i32* %".2"
  %".46" = alloca [19 x i8]
  store [19 x i8] c"a = a / 2, a = %d\0a\00", [19 x i8]* %".46"
  %".48" = getelementptr [19 x i8], [19 x i8]* %".46", i32 0, i32 0
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".45")
  %".50" = load i32, i32* %".2"
  store i32 7, i32* %".2"
  %".52" = load i32, i32* %".2"
  %".53" = load i32, i32* %".2"
  %".54" = srem i32 %".53", 4
  store i32 %".54", i32* %".2"
  %".56" = load i32, i32* %".2"
  %".57" = alloca [27 x i8]
  store [27 x i8] c"a = 7, a = a %% 4, a = %d\0a\00", [27 x i8]* %".57"
  %".59" = getelementptr [27 x i8], [27 x i8]* %".57", i32 0, i32 0
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59", i32 %".56")
  %".61" = alloca i32
  %".62" = alloca [32 x i8]
  store [32 x i8] c"\0a=====Start test operator=====\0a\00", [32 x i8]* %".62"
  %".64" = getelementptr [32 x i8], [32 x i8]* %".62", i32 0, i32 0
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64")
  %".66" = load i32, i32* %".61"
  store i32 1, i32* %".61"
  %".68" = load i32, i32* %".61"
  %".69" = alloca [8 x i8]
  store [8 x i8] c"b = %d\0a\00", [8 x i8]* %".69"
  %".71" = getelementptr [8 x i8], [8 x i8]* %".69", i32 0, i32 0
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".71", i32 %".68")
  %".73" = load i32, i32* %".61"
  %".74" = add i32 %".73", 1
  store i32 %".74", i32* %".61"
  %".76" = load i32, i32* %".61"
  %".77" = alloca [16 x i8]
  store [16 x i8] c"b += 1, b = %d\0a\00", [16 x i8]* %".77"
  %".79" = getelementptr [16 x i8], [16 x i8]* %".77", i32 0, i32 0
  %".80" = call i32 (i8*, ...) @"printf"(i8* %".79", i32 %".76")
  %".81" = load i32, i32* %".61"
  %".82" = sub i32 %".81", 1
  store i32 %".82", i32* %".61"
  %".84" = load i32, i32* %".61"
  %".85" = alloca [16 x i8]
  store [16 x i8] c"b -= 1, b = %d\0a\00", [16 x i8]* %".85"
  %".87" = getelementptr [16 x i8], [16 x i8]* %".85", i32 0, i32 0
  %".88" = call i32 (i8*, ...) @"printf"(i8* %".87", i32 %".84")
  %".89" = load i32, i32* %".61"
  %".90" = mul i32 %".89", 2
  store i32 %".90", i32* %".61"
  %".92" = load i32, i32* %".61"
  %".93" = alloca [16 x i8]
  store [16 x i8] c"b *= 2, b = %d\0a\00", [16 x i8]* %".93"
  %".95" = getelementptr [16 x i8], [16 x i8]* %".93", i32 0, i32 0
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".95", i32 %".92")
  %".97" = load i32, i32* %".61"
  %".98" = sdiv i32 %".97", 2
  store i32 %".98", i32* %".61"
  %".100" = load i32, i32* %".61"
  %".101" = alloca [16 x i8]
  store [16 x i8] c"b /= 2, b = %d\0a\00", [16 x i8]* %".101"
  %".103" = getelementptr [16 x i8], [16 x i8]* %".101", i32 0, i32 0
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", i32 %".100")
  %".105" = load i32, i32* %".61"
  store i32 7, i32* %".61"
  %".107" = load i32, i32* %".61"
  %".108" = srem i32 %".107", 4
  store i32 %".108", i32* %".61"
  %".110" = load i32, i32* %".61"
  %".111" = alloca [24 x i8]
  store [24 x i8] c"b = 7, b %%= 4, b = %d\0a\00", [24 x i8]* %".111"
  %".113" = getelementptr [24 x i8], [24 x i8]* %".111", i32 0, i32 0
  %".114" = call i32 (i8*, ...) @"printf"(i8* %".113", i32 %".110")
  %".115" = alloca [29 x i8]
  store [29 x i8] c"\0a=====Start arithmetic=====\0a\00", [29 x i8]* %".115"
  %".117" = getelementptr [29 x i8], [29 x i8]* %".115", i32 0, i32 0
  %".118" = call i32 (i8*, ...) @"printf"(i8* %".117")
  %".119" = add i32 23, 5
  %".120" = alloca [21 x i8]
  store [21 x i8] c"23+5 = %d (wait 28)\0a\00", [21 x i8]* %".120"
  %".122" = getelementptr [21 x i8], [21 x i8]* %".120", i32 0, i32 0
  %".123" = call i32 (i8*, ...) @"printf"(i8* %".122", i32 %".119")
  %".124" = mul i32 3, 4
  %".125" = alloca [20 x i8]
  store [20 x i8] c"3*4 = %d (wait 12)\0a\00", [20 x i8]* %".125"
  %".127" = getelementptr [20 x i8], [20 x i8]* %".125", i32 0, i32 0
  %".128" = call i32 (i8*, ...) @"printf"(i8* %".127", i32 %".124")
  %".129" = sub i32 6, 4
  %".130" = sub i32 22, %".129"
  %".131" = alloca [25 x i8]
  store [25 x i8] c"22-(6-4) = %d (wait 20)\0a\00", [25 x i8]* %".131"
  %".133" = getelementptr [25 x i8], [25 x i8]* %".131", i32 0, i32 0
  %".134" = call i32 (i8*, ...) @"printf"(i8* %".133", i32 %".130")
  %".135" = sdiv i32 6, 3
  %".136" = sdiv i32 22, %".135"
  %".137" = alloca [25 x i8]
  store [25 x i8] c"22/(6/3) = %d (wait 11)\0a\00", [25 x i8]* %".137"
  %".139" = getelementptr [25 x i8], [25 x i8]* %".137", i32 0, i32 0
  %".140" = call i32 (i8*, ...) @"printf"(i8* %".139", i32 %".136")
  %".141" = add i32 2, 1
  %".142" = sub i32 5, 2
  %".143" = mul i32 %".142", 4
  %".144" = sdiv i32 %".143", %".141"
  %".145" = add i32 1, %".144"
  %".146" = alloca [31 x i8]
  store [31 x i8] c"1+(5-2)*4/(2+1) = %d (wait 5)\0a\00", [31 x i8]* %".146"
  %".148" = getelementptr [31 x i8], [31 x i8]* %".146", i32 0, i32 0
  %".149" = call i32 (i8*, ...) @"printf"(i8* %".148", i32 %".145")
  %".150" = add i32 1, 23
  %".151" = sdiv i32 %".150", 4
  %".152" = mul i32 %".151", 5
  %".153" = mul i32 %".152", 67
  %".154" = add i32 0, %".153"
  %".155" = sub i32 %".154", 8
  %".156" = add i32 %".155", 9
  %".157" = alloca [38 x i8]
  store [38 x i8] c"0+(1+23)/4*5*67-8+9 = %d (wait 2011)\0a\00", [38 x i8]* %".157"
  %".159" = getelementptr [38 x i8], [38 x i8]* %".157", i32 0, i32 0
  %".160" = call i32 (i8*, ...) @"printf"(i8* %".159", i32 %".156")
  %".161" = sdiv i32 33, 5
  %".162" = mul i32 4, %".161"
  %".163" = mul i32 3, 8
  %".164" = add i32 %".163", %".162"
  %".165" = sdiv i32 192, %".164"
  %".166" = sub i32 %".165", 5
  %".167" = alloca [37 x i8]
  store [37 x i8] c"192/(3*8+4*(33/5))-5 = %d (wait -1)\0a\00", [37 x i8]* %".167"
  %".169" = getelementptr [37 x i8], [37 x i8]* %".167", i32 0, i32 0
  %".170" = call i32 (i8*, ...) @"printf"(i8* %".169", i32 %".166")
  ret i32 0
}
