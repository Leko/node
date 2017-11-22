// Copyright 2017 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Generated by tools/bigint-tester.py.

// Flags: --harmony-bigint

var data = [{
  a: "abde23cae3113c95ec7f444c7277658",
  b: "-65e40fb1",
  r: "-abde23cae3113c95ec7f444a2c379e9"
}, {
  a: "2d0bbdc05059c78b7e9f43689b2f7a9afaefd679212c2a9b990",
  b: "29fcdb109b54650f9762b494916bc1cf14853430697febe7acf4327983ce0c6c4c183",
  r: "29fcdb109b54650f974fbf29513b98089ffbab7301e4c49d360eddaffaef2046d7813"
}, {
  a: "b958dc77068d01811e031d6320df5e53823697be94f7654340b",
  b: "-c1f5ca609a658e24fc33fec10a84b18fb745cb7c6",
  r: "-b958dc77064cf44b7e9978ed04236dad433c130f1b4020883cf"
}, {
  a: "cf7319e3fe16912370c830906f88b",
  b: "98d972f3c",
  r: "cf7319e3fe16912370c8a8491d7b7"
}, {
  a: "aea6d9e7cec74bca19",
  b: "5abbcd0c5aa1f96fef9db32b3618de782db64b8f6b4",
  r: "5abbcd0c5aa1f96fef9db32b3cf2b3e6515a3f33cad"
}, {
  a: "-b522a022e90fa094f3b729a7a0a914349f5e1fd778829d7576ad36711",
  b: "-aa00d2fd6a7636",
  r: "b522a022e90fa094f3b729a7a0a914349f5e1fd778883d78597b91125"
}, {
  a: "9c2bc822ec4a590eb8a77ee630009713090",
  b: "30b13459c1434",
  r: "9c2bc822ec4a590eb8a77ed68134ced24a4"
}, {
  a: "-f14873e1f6121d584d5541073c7ce162873e156b72fb3c943ffd5f212c0d6",
  b: "f449f0a292048546924d2973626f5441c045d4adbfd00d301791f0db965f",
  r: "-fe0cecebdf32550c247193900a5a14269b3a4821a9063c473e84402c9568b"
}, {
  a: "83d5552fba4213d8dd1ed9bc6c2",
  b: "4f7ccc10ba9b6880b862f8d5e1c9",
  r: "47419942413f49bd35b3154e270b"
}, {
  a: "9fdb44741177921c8338b70fc7fa362295bfc92f6275fa16492",
  b: "93676e5ef972",
  r: "9fdb44741177921c8338b70fc7fa362295bfc92654031ff9de0"
}, {
  a: "4355637ed",
  b: "-7aeb3013cc5eb39d56eed8104407a3e68039944f7673a0c75bd3",
  r: "-7aeb3013cc5eb39d56eed8104407a3e68039944f767795916c40"
}, {
  a: "7fdf50188f716c13feced67a1c33ecf422",
  b: "-7106cd7b9",
  r: "-7fdf50188f716c13feced67a1b2380239b"
}, {
  a: "368cf8d0f5790a03774b9a1e116f82281ebd9e18de7f54a7d91f50",
  b: "8bc4e4f24ce2a7d037079552e6c7db2795f15c92a01f4e0d9",
  r: "368cf06cbb362ecd5d36996e683aac44630fe747cbb67ea62dff89"
}, {
  a: "-7466a596078a20cc4eca96953e3",
  b: "-666328e5437b1475dcfe2f44f1c6a82af82ce7ee7cf229c8398836d2d834f9014",
  r: "666328e5437b1475dcfe2f44f1c6a82af82ce79a1a57bfcfb3a8fa9c12a26c3f1"
}, {
  a: "ad284b70a22d96bdefba53f134c65a1e4958013bb9a31f091fde6fc89",
  b: "-c89374df2",
  r: "-ad284b70a22d96bdefba53f134c65a1e4958013bb9a31f09d74d1b179"
}, {
  a: "-47df52354db5",
  b: "-aa7f61aba9ad859e803e964418af30",
  r: "aa7f61aba9ad859e807949162de29b"
}, {
  a: "-f03ea80f22a3dc03f036b13f85faf5fb1",
  b: "86e9110772d369fdd52b45a8fb22cea26cb73e908408f8a3cdf637f0042c8efdc11",
  r: "-86e9110772d369fdd52b45a8fb22cea26c4700388b2a5b7fce0601413ba974083a2"
}, {
  a: "3603d29c8",
  b: "f4849ec3ec3c352b",
  r: "f4849ec08c011ce3"
}, {
  a: "e6668ed8eae8b4bb7bdf522d44e9f1bcf66",
  b: "361cab4f5be1",
  r: "e6668ed8eae8b4bb7bdf522e25234549487"
}, {
  a: "-d0395d",
  b: "-4a8ee89d006d22a124070241caf5f4343bdfd30d12",
  r: "4a8ee89d006d22a124070241caf5f4343bdf03344d"
}];

var error_count = 0;
for (var i = 0; i < data.length; i++) {
  var d = data[i];
  var a = BigInt.parseInt(d.a, 16);
  var b = BigInt.parseInt(d.b, 16);
  var r = a ^ b;
  if (d.r !== r.toString(16)) {
    print("Input A:  " + a.toString(16));
    print("Input B:  " + b.toString(16));
    print("Result:   " + r.toString(16));
    print("Expected: " + d.r);
    print("Op: ^");
    error_count++;
  }
}
if (error_count !== 0) {
  print("Finished with " + error_count + " errors.")
  quit(1);
}
