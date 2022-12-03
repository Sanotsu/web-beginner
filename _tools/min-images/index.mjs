import imagemin from 'imagemin';
import imageminJpegtran from 'imagemin-jpegtran';
import imageminPngquant from 'imagemin-pngquant';

/**
 * 压缩图片质量，减少体积。
 * 图片放在images下，输出在output中
 */

const files = await imagemin(['input/*.{jpg,png,jpeg}'], {
    destination: 'output',
    plugins: [
        imageminJpegtran({
            quality: [0.6, 0.8]
        }),
        imageminPngquant({
            quality: [0.6, 0.8]
        })
    ]
});

console.log(files);
//=> [{data: <Buffer 89 50 4e …>, destinationPath: 'build/images/foo.jpg'}, …]